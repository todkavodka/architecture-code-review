import httpx


def deliver_webhook(target_url: str, payload: dict) -> None:
    """Send an integration event.

    UNKNOWN-1 is intentional: this fixture does not include the configuration loader,
    API route, admin UI, or deployment source that supplies target_url. The sink is real,
    but attacker control of the destination cannot be established from available evidence.
    """
    httpx.post(target_url, json=payload, timeout=5.0)
