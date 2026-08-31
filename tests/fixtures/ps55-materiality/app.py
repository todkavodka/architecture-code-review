from fastapi import FastAPI, Depends, HTTPException, Query

from .db import get_document_by_id, search_documents_unsafe, list_documents_sorted
from .models import User

app = FastAPI()


def current_user() -> User:
    # Fixture simplification: caller is authenticated, but resource authorization remains separate.
    return User(id=7, workspace_id=3, role="member")


@app.get("/documents/{document_id}")
def read_document(document_id: int, user: User = Depends(current_user)):
    document = get_document_by_id(document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="not found")
    # REAL-1: authentication exists, but no owner/workspace authorization is checked.
    return document


@app.get("/documents/search")
def search_documents(q: str = Query(...), user: User = Depends(current_user)):
    return search_documents_unsafe(q)


@app.get("/documents")
def list_documents(sort: str = "created", user: User = Depends(current_user)):
    # SAFE-1 lives in the DB helper: sort is mapped to an internal allowlist before raw SQL.
    return list_documents_sorted(sort, workspace_id=user.workspace_id)
