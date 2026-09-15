<!--
  SPDX-License-Identifier: GPL-3.0-or-later
  Copyright (c) 2026 SnapKittyWest
  Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
  CLONE GATE: Any clone, fork, or derivative of this node
  MUST be released under GPL-3.0-or-later. No closed-source use.
-->

# Counterexamples — Black Book Engine

RULE: Every formal model MUST have at least one defined failure case.  
A theory without falsification criteria MUST NOT be counted as a completed contribution.

---

## Failure Cases by Formal Object

### SYMBOLIC_STATE_SYSTEM S = (N, E, T, R, I)
**Failure Case:** A symbol relationship exists in the source that cannot be labeled by any element of L = { PRECEDES, FOLLOWS, CONTAINS, TRANSFORMS, OPPOSES, MERGES, SEPARATES, REPEATS, DISAPPEARS, REAPPEARS, INTERRUPTS, RESOLVES, FAILS_TO_RESOLVE }.  
**Consequence:** L must be extended; this is an ONTOLOGY_EXTENSION_EVENT, not a model failure.  
**Detection:** During extraction step 3, flag any relationship that cannot be mapped to L.

### TEMPORAL_ASSIGNMENT_FUNCTION T
**Failure Case:** A symbol appears in an undated entry, making T(n) undefined.  
**Consequence:** Node must be recorded in TEMPORAL_AMBIGUITY_LOG with T(n) = UNDEFINED.  
**Detection:** Any entry in the Black Books that lacks a date or unambiguous page reference.

### SYMBOL_TRANSITION_FUNCTION F
**Failure Case:** F is everywhere undefined — no systematic transitions exist.  
**Consequence:** The transition model is inapplicable to the Black Books material; F must be replaced with a weaker structure.  
**Detection:** For each observed symbolic event x, check whether F(s, x) produces any consistent output.

### SYMBOL_RESONANCE
**Failure Case:** All symbol pairs have identical RESONANCE values.  
**Consequence:** The metric has no discriminative power — must be revised or abandoned.  
**Detection:** Compute RESONANCE for all pairs; check variance. If variance ≈ 0, metric fails.

### SYMBOL_DRIFT
**Failure Case:** No symbol shows DRIFT > threshold_stable.  
**Consequence:** The text is symbolically static (no contextual transformations) — this is a positive research finding, not an error.  
**Detection:** Compute SEMANTIC_DRIFT for all symbols; count those exceeding threshold.

### SYMBOL_INVERSION
**Failure Case:** Condition (4) — explicit textual generation of n' from n — is never satisfied for any symbol pair.  
**Consequence:** INVERSION is an empty operator; formally the text contains no attested symbolic inversions.  
**Detection:** Search for explicit generation statements in dialogues and vision sequences.

### SYMBOL_ENTROPY H(t)
**Failure Case:** H(t) shows no correlation with any narrative complexity markers.  
**Consequence:** The entropy model has no explanatory power for this material; either the markers are wrong or the model is wrong.  
**Detection:** Correlation coefficient between H(t) and annotated narrative complexity markers; test against null hypothesis of zero correlation.

### SYMBOL_ATTRACTOR
**Failure Case:** No symbol satisfies all three criteria simultaneously.  
**Consequence:** No attractors exist in the model as defined; either lower the thresholds or accept that the Black Books has no symbol attractors.  
**Detection:** Apply all three criteria to all nodes; count nodes satisfying all three.

### H_COLLAPSE Hypothesis
**Failure Case:** NET_RATE is not significantly negative in the final 10% of T_total.  
**Consequence:** H_COLLAPSE is falsified; the terminal interruption is not preceded by symbolic withdrawal.  
**Detection:** Mann-Whitney U test on NET_RATE in final 10% vs remainder.

### TRANSFORMATION_MONOID M(R)
**Failure Case:** M(R) is commutative (R_i ∘ R_j = R_j ∘ R_i for all observed pairs).  
**Consequence:** The monoid is commutative — a different algebraic structure than hypothesized; record as finding.  
**Detection:** Test commutativity for all observed compound transformation pairs.

### G_opp BIPARTITENESS
**Failure Case 1:** G_opp is bipartite — clean dual opposition structure exists.  
**Consequence:** Record bipartiteness as structural finding; this is not a failure of the model but an empirical result.  
**Detection:** 2-coloring algorithm on G_opp.

**Failure Case 2:** G_opp has no edges — no attested oppositions in the source.  
**Consequence:** Source annotation failed to identify oppositions; return to extraction step 3.

### SYMBOLIC_LANGUAGE L(TSA)
**Failure Case:** L(A) is regular (Myhill-Nerode theorem confirms finite number of equivalence classes).  
**Consequence:** Symbolic dynamics are regular (FSM-describable); a simpler model suffices.  
**Detection:** Apply Myhill-Nerode theorem to observed symbol sequences.

### INTERRUPTION_GRAPH G_I
**Failure Case:** G_I is an Erdős-Rényi random graph (no clustering in interruption events).  
**Consequence:** Interruption events share no structural features; the interruption network is uninformative.  
**Detection:** Compare G_I clustering coefficient to random graph baseline; chi-squared test.

### TU TERMINAL UNRESOLVED SEQUENCE
**Failure Case:** The terminal break is editorial rather than authorial.  
**Consequence:** The interruption model is applied to the wrong object — a SOURCE_VERIFICATION_FAILURE.  
**Detection:** Cross-reference Shamdasani's editorial notes with manuscript evidence.

---

*STATUS: RESEARCH_IN_PROGRESS | 14 failure cases defined | Awaiting empirical testing*
