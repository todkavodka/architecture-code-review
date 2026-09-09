# PS-155 — Stage F consumer/provider link

## Design mapping

`PS-F02`: an exact internal consumer call becomes a consumed IF and INT linked
to the evidenced provider revision.

## Setup / evidence shape

Service B makes an exact call to Service A’s accepted `GET /orders/{id}`
operation. Consumer source evidence is `STRONG_INFERENCE` or
`DIRECT_DECLARATION`, with exact operation and Project/revision binding; the
provider IF is independently accepted at its own exact revision.

## Expected accepted semantic records

The Technical Model Gate may accept a consumed `IF-*` for Service B with
`direction=CONSUMED`, `contract_role=CONSUMER_OBSERVED_USE` or
`CONSUMER_EXPECTATION` as evidenced, and an `INT-*` with `interaction_kind=CALL`
referencing the consumer IF and the qualified provider IF. Provider and
consumer identities remain separate.

## Prohibited inference / authority result

- same path or method alone cannot establish the link;
- a consumer IF cannot be rewritten as the provider IF;
- candidate matching cannot become compatibility;
- an INT cannot be accepted from projection prose.

## Expected projection behavior

Consumed-interface and integration projections show the consumer IF, exact
provider reference when evidenced, concrete INT, revisions, and limitations.
The Product view, if selected, preserves both Project qualifications.

## Backward-compatibility constraint

Historical consumer IFs without provider references remain valid and visibly
unmatched; the new qualified link is additive and does not rewrite old IDs.

## GREEN criteria

GREEN iff the consumer IF and INT are accepted with exact evidence and separate
provider/consumer identities, the link is not inferred from name similarity,
and all projections preserve both revisions and provenance.

## Verdict

`PS155_PASS_CONSUMER_PROVIDER_LINK`
