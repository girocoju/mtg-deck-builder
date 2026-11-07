# Janela flutuante do assistente de draft (WinForms, sem dependências além do Windows).
# Lê o arquivo indicado a cada meio segundo: a primeira linha é o instante (Unix, segundos)
# em que o Python escreveu; o resto é o texto. Se o Python parar de escrever por mais de
# 8 s, a janela se fecha sozinha. Teclas: Esc fecha, + e - mudam a fonte, F troca de canto.
param(
    [string]$Path,
    [string]$Title = "Draft",
    [int]$Width = 720,
    [int]$Height = 760,
    [double]$Opacity = 0.93,
    [int]$FontSize = 10
)
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$form = New-Object System.Windows.Forms.Form
$form.Text = $Title
$form.TopMost = $true
$form.Opacity = $Opacity
$form.BackColor = [System.Drawing.Color]::FromArgb(16, 20, 24)
$form.StartPosition = "Manual"
$form.Size = New-Object System.Drawing.Size($Width, $Height)
$form.KeyPreview = $true
$area = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$script:right = $true
function Place-Window {
    if ($script:right) { $x = $area.Right - $Width - 16 } else { $x = $area.Left + 16 }
    $form.Location = New-Object System.Drawing.Point($x, ($area.Top + 40))
}
Place-Window

$box = New-Object System.Windows.Forms.TextBox
$box.Multiline = $true
$box.ReadOnly = $true
$box.WordWrap = $false
$box.ScrollBars = "Both"
$box.Dock = "Fill"
$box.BorderStyle = "None"
$box.BackColor = $form.BackColor
$box.ForeColor = [System.Drawing.Color]::FromArgb(232, 232, 232)
$script:size = $FontSize
$box.Font = New-Object System.Drawing.Font("Consolas", $script:size)
$box.Text = "aguardando o log do Arena..."
$form.Controls.Add($box)

$script:last = ""
$timer = New-Object System.Windows.Forms.Timer
$timer.Interval = 500
$timer.Add_Tick({
    try {
        if (-not (Test-Path -LiteralPath $Path)) { return }
        $raw = [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)
        $cut = $raw.IndexOf("`n")
        if ($cut -lt 0) { return }
        $stamp = [int64]($raw.Substring(0, $cut).Trim())
        $now = [System.DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
        if (($now - $stamp) -gt 8) { $form.Close(); return }
        $text = $raw.Substring($cut + 1)
        if ($text -ne $script:last) {
            $script:last = $text
            $box.Text = $text.Replace("`r`n", "`n").Replace("`n", "`r`n")
            $box.SelectionStart = 0
            $box.ScrollToCaret()
        }
    } catch { }
})
$timer.Start()

$form.Add_KeyDown({
    param($sender, $e)
    if ($e.KeyCode -eq [System.Windows.Forms.Keys]::Escape) { $form.Close() }
    elseif ($e.KeyCode -eq [System.Windows.Forms.Keys]::Add -or $e.KeyCode -eq [System.Windows.Forms.Keys]::Oemplus) {
        $script:size = [Math]::Min(18, $script:size + 1)
        $box.Font = New-Object System.Drawing.Font("Consolas", $script:size)
    }
    elseif ($e.KeyCode -eq [System.Windows.Forms.Keys]::Subtract -or $e.KeyCode -eq [System.Windows.Forms.Keys]::OemMinus) {
        $script:size = [Math]::Max(7, $script:size - 1)
        $box.Font = New-Object System.Drawing.Font("Consolas", $script:size)
    }
    elseif ($e.KeyCode -eq [System.Windows.Forms.Keys]::F) { $script:right = -not $script:right; Place-Window }
})
[void]$form.ShowDialog()
