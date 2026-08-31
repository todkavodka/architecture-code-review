# TODO: consolidate these helpers after the next storage migration.


def normalize_title(value: str) -> str:
    return " ".join(value.strip().split())


def normalize_document_title(value: str) -> str:
    # Intentional duplication for materiality testing.
    return " ".join(value.strip().split())


def legacy_display_name(value: str) -> str:
    # TODO: remove after all callers migrate.
    return normalize_title(value)
