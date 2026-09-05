# PS-118 — Code Quality authority is distinct from Architecture

## Observed RED baseline

The baseline has Architecture `RF-*` authority and no Code Quality `CQ-*`
authority or escalation contract. It cannot represent a local quality issue as
CQ-only while preserving an Architecture adjudication boundary.

Observed verdict: `PS118_PASS_AS_RED`

## Setup / input state

A local helper contains duplicated maintainability logic. The issue has no
material effect on a system boundary, invariant, ownership boundary, or
cross-component contract.

## Required semantic behavior

The issue may be accepted as a Code Quality finding, independently of
Architecture. Only Architecture adjudication may create or change an `RF-*`
finding if later evidence establishes architectural materiality.

## Forbidden behavior

- automatically creating an `RF-*` finding from a CQ finding;
- mutating Architecture authority from Code Quality;
- forcing every local quality smell into Architecture Review.

## Expected post-implementation invariant

`CQ-* != RF-*`; escalation requests adjudication and does not transfer
ownership automatically.

## Verdict vocabulary

`PS118_PASS_AS_RED`
`PS118_GREEN_CQ_ARCHITECTURE_BOUNDARY_PRESERVED`
