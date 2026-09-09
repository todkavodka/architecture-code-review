# PS-170 — Stage F secret connection redaction

## Design mapping

`PS-F17`: a secret-bearing connection string is referenced safely without
secret output.

## Setup / evidence shape

Evidence identifies a synthetic credential-bearing connection source using only
the placeholder `postgresql://<redacted>@db.example.invalid/<redacted>`. The
underlying value is classified `SECRET`; the record retains a safe source
pointer, technology/logical-store fact, and redaction limitation only.

## Expected accepted semantic records

The Technical Model Gate may accept a safe logical DS/store identity and a
bounded limitation when independently supported. It must not accept or persist
the credential, token, password, or complete secret-bearing DSN.

## Prohibited inference / authority result

- `SECRET` values must never be copied into EV, STM, PRJ, fingerprint, or
  package output;
- a connection string alone does not prove table access;
- redaction is owned by the evidence/safety contracts, not by a catalog;
- no realistic live credential is included.

## Expected projection behavior

Service and Product projections omit the secret value and may render only the
technology, logical store, safe endpoint class, source pointer, and limitation.

## Backward-compatibility constraint

Existing safe provenance pointers remain usable. Historical records are not
bulk-rewritten; missing safe qualifiers remain absent until bounded revalidation.

## GREEN criteria

GREEN iff no secret value appears in any scenario or projected representation,
the safe logical fact remains useful, and connection presence is not promoted
to precise access.

## Verdict

`PS170_PASS_SECRET_REDACTION`
