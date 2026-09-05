# PS-125 — Security escalation does not transfer ownership

## Observed RED baseline

The baseline has no Code Quality security-routing contract. There is no
dedicated Security capability; security-relevant concerns currently use
existing Architecture/security semantics, but no CQ relation or handoff rule
exists.

Observed verdict: `PS125_PASS_AS_RED`

## Setup / input state

A quality review observes a hardcoded secret, unsafe deserialization, weak
crypto, unsafe subprocess, authorization race, or dangerous default with a
credible security consequence.

## Required semantic behavior

Code Quality may preserve an independent quality interpretation and may
correlate or request escalation to existing Architecture/security adjudication.
The receiving authority decides its own security meaning and severity.

## Forbidden behavior

- inventing a dedicated Security capability;
- creating or mutating Architecture security authority directly;
- downgrading, closing, or suppressing the security interpretation from CQ.

## Expected post-implementation invariant

Security escalation is an adjudication request or explicit relation, not an
ownership transfer; security relevance is never downgraded by CQ.

## Verdict vocabulary

`PS125_PASS_AS_RED`
`PS125_GREEN_SECURITY_HANDOFF_PRESERVED`
