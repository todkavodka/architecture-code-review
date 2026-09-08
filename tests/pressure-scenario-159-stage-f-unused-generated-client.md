# PS-159 — Stage F unused generated client

## Design mapping

`PS-F06`: an unused generated client does not become an external integration.

## Setup / evidence shape

A repository contains generated client code for an external API, but no call
site, configured execution path, test use, or declaration establishes that the
client is used. The generated artifact is a `WEAK_HINT` with an explicit
unused/unverified limitation.

## Expected accepted semantic records

The Technical Model Gate may retain the generated-client observation. It must
not accept a consumed IF, concrete CALL INT, provider identity, or external
integration from the unused client alone.

## Prohibited inference / authority result

- generated client exists != client method use;
- dependency presence does not prove runtime integration;
- an unused type or endpoint cannot establish provider/consumer compatibility;
- projections cannot promote the hint.

## Expected projection behavior

Technical Documentation either omits the non-factual client from integration
facts or shows it only as a bounded weak hint. It does not list an accepted
external interaction.

## Backward-compatibility constraint

Historical generated artifacts remain observations with their original scope;
later call evidence is additive and does not rewrite prior evidence meaning.

## GREEN criteria

GREEN iff no accepted IF/INT/provider is produced from the unused client, the
weak-hint limitation is preserved, and all projections remain derived from
accepted STM facts.

## Verdict

`PS159_PASS_UNUSED_CLIENT_BOUNDARY`
