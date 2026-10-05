"""Consultas à base local de cartas."""

# Layouts que não são cartas jogáveis em deck.
EXTRA_LAYOUTS = ("token", "double_faced_token", "emblem", "art_series")

ORDERS = {
    "name": "c.name",
    "cmc": "c.cmc, c.name",
    "edhrec": "c.edhrec_rank IS NULL, c.edhrec_rank",
}


def search(conn, *, name=None, text=None, type_line=None, identity=None, colors=None,
           fmt=None, set_code=None, rarity=None, game=None, booster=False,
           cmc_min=None, cmc_max=None, include_extras=False, order="name", limit=50):
    """Busca cartas. `identity` filtra por identidade contida nas cores dadas
    (regra de Commander/Brawl); `colors` exige que a carta tenha todas as cores dadas."""
    where, params = [], []

    if name:
        where.append("c.name LIKE ?")
        params.append(f"%{name}%")
    if text:
        where.append("c.oracle_id IN (SELECT oracle_id FROM cards_fts WHERE cards_fts MATCH ?)")
        params.append(text)
    for word in (type_line or "").split():
        where.append("c.type_line LIKE ?")
        params.append(f"%{word}%")
    if identity is not None:
        where.append("subset(c.color_identity, ?)")
        params.append(identity.upper().replace("C", ""))
    if colors:
        where.append("subset(?, c.colors)")
        params.append(colors.upper())
    if fmt:
        where.append(
            "EXISTS (SELECT 1 FROM legalities l WHERE l.oracle_id = c.oracle_id "
            "AND l.format = ? AND l.status IN ('legal', 'restricted'))"
        )
        params.append(fmt.lower())
    if cmc_min is not None:
        where.append("c.cmc >= ?")
        params.append(cmc_min)
    if cmc_max is not None:
        where.append("c.cmc <= ?")
        params.append(cmc_max)
    if not include_extras:
        where.append(f"c.layout NOT IN ({','.join('?' * len(EXTRA_LAYOUTS))})")
        params.extend(EXTRA_LAYOUTS)

    printing = []
    if set_code:
        printing.append("p.set_code = ?")
        params.append(set_code.lower())
    if rarity:
        printing.append("p.rarity = ?")
        params.append(rarity.lower())
    if game:
        printing.append("instr(p.games, ?) > 0")
        params.append(game.lower())
    if booster:
        printing.append("p.booster = 1")
    if printing:
        where.append(
            "EXISTS (SELECT 1 FROM printings p WHERE p.oracle_id = c.oracle_id AND "
            + " AND ".join(printing) + ")"
        )

    sql = "SELECT c.* FROM cards c"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += f" ORDER BY {ORDERS[order]} LIMIT ?"
    params.append(limit)
    return conn.execute(sql, params).fetchall()


def find_card(conn, name):
    """Carta por nome exato (aceita só a face da frente); senão, candidatas por trecho."""
    rows = conn.execute(
        "SELECT * FROM cards WHERE (name = ?1 COLLATE NOCASE OR name LIKE ?1 || ' // %') "
        f"AND layout NOT IN ({','.join('?' * len(EXTRA_LAYOUTS))})",
        (name, *EXTRA_LAYOUTS),
    ).fetchall()
    if len(rows) == 1:
        return rows[0], []
    return None, rows or search(conn, name=name, limit=20)


def legalities(conn, oracle_id):
    return dict(conn.execute(
        "SELECT format, status FROM legalities WHERE oracle_id = ? ORDER BY format", (oracle_id,)
    ).fetchall())


def printings(conn, oracle_id):
    return conn.execute(
        "SELECT * FROM printings WHERE oracle_id = ? ORDER BY released_at DESC", (oracle_id,)
    ).fetchall()


def rulings(conn, oracle_id):
    return conn.execute(
        "SELECT published_at, comment FROM rulings WHERE oracle_id = ? ORDER BY published_at",
        (oracle_id,),
    ).fetchall()


def find_sets(conn, term=None):
    """Coleções por código exato ou trecho do nome, mais recentes primeiro."""
    if term:
        return conn.execute(
            "SELECT * FROM sets WHERE code = ?1 COLLATE NOCASE OR name LIKE '%' || ?1 || '%' "
            "ORDER BY released_at DESC",
            (term,),
        ).fetchall()
    return conn.execute("SELECT * FROM sets ORDER BY released_at DESC").fetchall()


def set_rarity_counts(conn, set_code, booster_only=True):
    return dict(conn.execute(
        "SELECT rarity, COUNT(DISTINCT oracle_id) FROM printings "
        "WHERE set_code = ? AND booster >= ? GROUP BY rarity",
        (set_code.lower(), int(booster_only)),
    ).fetchall())


def stats(conn):
    out = {
        table: conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        for table in ("cards", "printings", "sets", "rulings")
    }
    out["formats"] = [r[0] for r in conn.execute("SELECT DISTINCT format FROM legalities")]
    out.update(dict(conn.execute("SELECT key, value FROM meta").fetchall()))
    return out
