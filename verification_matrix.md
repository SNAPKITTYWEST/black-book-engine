<!--
  SPDX-License-Identifier: GPL-3.0-or-later
  Copyright (c) 2026 SnapKittyWest
  Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
  CLONE GATE: Any clone, fork, or derivative of this node
  MUST be released under GPL-3.0-or-later. No closed-source use.
-->

# Verification Matrix — Black Book Engine

STATUS: RESEARCH_IN_PROGRESS  
RULE: Every formal claim MUST have a test record.  
FORMAT: CLAIM | INPUT | EXPECTED_PROPERTY | EXECUTION | OBSERVED_PROPERTY | RESULT

---

## Test Records

### TC-001
**CLAIM:** The RESONANCE_MATRIX R has dominant eigenvectors corresponding to interpretable symbol clusters.  
**INPUT:** RESONANCE_MATRIX computed over 50 symbols from Black Books.  
**EXPECTED_PROPERTY:** Dominant eigenvectors (top 5) partition N into non-trivial clusters (size > 1) with interpretable content.  
**EXECUTION:** Compute R; eigendecomposition; k-means on eigenvectors.  
**OBSERVED_PROPERTY:** TBD (requires primary source data)  
**RESULT:** PENDING

---

### TC-002
**CLAIM:** SYMBOL_ENTROPY H(t) is higher during extended vision sequences than during transitional passages.  
**INPUT:** H(t) time series; annotation of vision sequence periods vs transitional periods.  
**EXPECTED_PROPERTY:** mean H(vision_periods) > mean H(transitional_periods).  
**EXECUTION:** Compute H(t); annotate text; Mann-Whitney U test.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-003
**CLAIM:** The opposition subgraph G_opp is NOT bipartite.  
**INPUT:** G_opp extracted from symbol graph.  
**EXPECTED_PROPERTY:** G_opp contains at least one odd cycle.  
**EXECUTION:** Bipartiteness test (2-coloring algorithm).  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-004
**CLAIM:** SYMBOL_PRODUCTION_RATE is higher in the first notebook (BB-1) than in subsequent notebooks.  
**INPUT:** T_first for all n; notebook boundaries.  
**EXPECTED_PROPERTY:** ENTRY_RATE(t ∈ BB-1) > ENTRY_RATE(t ∈ BB-k for k>1).  
**EXECUTION:** Compute ENTRY_RATE per notebook; ANOVA.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-005
**CLAIM:** Symbols in TERMINAL_ORPHAN_SYMBOLS have higher RESONANCE with n_Philemon than non-orphan symbols.  
**INPUT:** TERMINAL_ORPHAN_SYMBOLS set; RESONANCE matrix.  
**EXPECTED_PROPERTY:** mean RESONANCE(orphan, n_Philemon) > mean RESONANCE(non-orphan, n_Philemon).  
**EXECUTION:** Extract sets; compute mean resonances; t-test.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-006
**CLAIM:** H_COLLAPSE — NET_RATE is significantly negative in the pre-terminal period (final 10% of T_total).  
**INPUT:** NET_RATE(t, k) for all t; T_terminal boundary.  
**EXPECTED_PROPERTY:** mean NET_RATE(t ∈ [0.9*T_total, T_total]) << mean NET_RATE(t ∈ [0, 0.9*T_total]).  
**EXECUTION:** Compute NET_RATE time series; split at 0.9*T_total; Mann-Whitney U test.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-007
**CLAIM:** The TRANSFORMATION_MONOID M(R) is non-commutative.  
**INPUT:** Three observed compound transformations from the text.  
**EXPECTED_PROPERTY:** R_i ∘ R_j ≠ R_j ∘ R_i for at least one pair.  
**EXECUTION:** Identify three compound transformations; check commutativity of each pair.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-008
**CLAIM:** SYMBOL_DRIFT is higher for the serpent figure than for stable background symbols.  
**INPUT:** CONTEXT(serpent, t) and CONTEXT(background, t) at multiple time points.  
**EXPECTED_PROPERTY:** SEMANTIC_DRIFT(serpent) > SEMANTIC_DRIFT(background_symbol).  
**EXECUTION:** Compute CONTEXT vectors at T_first and T_last; compute cosine distance.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-009
**CLAIM:** The Black Books symbol sequence is significantly more compressible than a random permutation.  
**INPUT:** Encoded symbol sequence; 100 random permutations of same sequence.  
**EXPECTED_PROPERTY:** compression_ratio(original) < mean(compression_ratio(permutations)) - 2*std.  
**EXECUTION:** Encode; apply gzip; compare to random permutation baseline.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

### TC-010
**CLAIM:** Named figures (N_NAMED) have higher degree centrality than unnamed figures (N_UNNAMED).  
**INPUT:** Degree for all n ∈ N_NAMED and n ∈ N_UNNAMED.  
**EXPECTED_PROPERTY:** Mann-Whitney U test significant at p < 0.05.  
**EXECUTION:** Compute degrees; split by naming; statistical test.  
**OBSERVED_PROPERTY:** TBD  
**RESULT:** PENDING

---

## FALSIFICATION_MATRIX

| Formal Object | Falsification Condition | If Falsified |
|---------------|------------------------|--------------|
| SYMBOL_RESONANCE | All resonance values identical | Metric has no discriminative power — revise |
| SYMBOL_DRIFT | No symbol shows DRIFT > threshold_stable | Text is symbolically static — record as finding |
| SYMBOL_INVERSION | Condition (4) never satisfied | INVERSION is empty operator — mark as failed |
| SYMBOL_ENTROPY H(t) | No correlation with narrative markers | Entropy model has no explanatory power — revise |
| SYMBOL_ATTRACTOR | No symbol satisfies all 3 criteria | No attractors in model — record as finding |
| SYMBOL_BOUNDARY ∂A | No closed cluster exists | Symbol graph is fully connected — record as finding |
| H_COLLAPSE | NET_RATE not negative in final 10% | H_COLLAPSE falsified — revise temporal model |
| TRANSFORMATION_MONOID | All R_i ∘ R_j = R_j ∘ R_i | Monoid is commutative — record algebraic structure |
| G_opp bipartite test | G_opp is bipartite | Clean dual opposition structure — record as finding |
| TSA language | L(A) is regular | Symbolic dynamics are regular — record |
| H_PRECURSOR | No symbol elevated in precursor windows | No interruption predictors — record as finding |

---

*STATUS: RESEARCH_IN_PROGRESS | 10 test records defined | PENDING primary source data*
