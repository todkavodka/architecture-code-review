import sqlite3

DB = sqlite3.connect(":memory:", check_same_thread=False)
DB.row_factory = sqlite3.Row

SORT_COLUMNS = {
    "created": "created_at",
    "title": "title",
}


def get_document_by_id(document_id: int):
    return DB.execute(
        "SELECT id, workspace_id, title, body FROM documents WHERE id = ?",
        (document_id,),
    ).fetchone()


def search_documents_unsafe(q: str):
    # REAL-2: request-controlled text is interpolated into executable SQL.
    sql = f"SELECT id, title FROM documents WHERE title LIKE '%{q}%'"
    return DB.execute(sql).fetchall()


def list_documents_sorted(sort: str, workspace_id: int):
    # SAFE-1: dynamic identifier is selected from an internal allowlist; data remains bound.
    column = SORT_COLUMNS.get(sort, SORT_COLUMNS["created"])
    sql = f"SELECT id, title FROM documents WHERE workspace_id = ? ORDER BY {column} DESC"
    return DB.execute(sql, (workspace_id,)).fetchall()
