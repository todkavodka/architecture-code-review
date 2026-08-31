from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    workspace_id: int
    role: str
