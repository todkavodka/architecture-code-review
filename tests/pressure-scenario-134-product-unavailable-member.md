# PS-134 — Product with an unavailable member

## Input state

An accepted Product revision has Projects A and B available and a required
Project C whose source or selected revision is unavailable.

## Expected semantic behavior

The baseline records C's source-availability limitation independently from the
available exact bindings. A and B's accepted local state remains addressable;
Product conclusions are bounded to evidence that is sufficient and disclose
the unavailable member where it matters.

## Forbidden behavior

- treating unavailable as failed;
- creating a negative finding solely because C cannot be read;
- collapsing all Product state into universal `PARTIAL` or `BLOCKED` status.

## Affected authority

Session/Product baseline routing records source availability. Existing
capability owners decide whether their semantic evidence is sufficient.

## Expected impact scope

Only Product records, relations, projections, or packages depending on C are
limited or escalated; unaffected A/B local state is preserved.

## Package/projection outcome

Required members or dependencies involving C may block a selected package;
unrelated Product or Project packages may remain usable under their own gates.

## Verdict

`PS134_PASS_INDEPENDENT_UNAVAILABLE_MEMBER`
