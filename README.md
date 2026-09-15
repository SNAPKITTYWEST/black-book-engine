<!--
  SPDX-License-Identifier: GPL-3.0-or-later
  Copyright (c) 2026 SnapKittyWest
  Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
  CLONE GATE: Any clone, fork, or derivative of this node
  MUST be released under GPL-3.0-or-later. No closed-source use.
-->

# Black Book Engine

**STATUS: RESEARCH_IN_PROGRESS**  
**BATCH: 01 | Lines: ~3,200 / 10,000 target**

A formal research framework for generating original contributions from structural analysis of Jung's Black Books / Liber Novus. This is NOT a summary of Jung. This is NOT a textbook. This is a new formal research layer.

---

## Objective

Generate a minimum of **10,000 substantive lines of original research contributions** derived from structural analysis of the Black Books / Liber Novus material.

Every contribution must introduce at least one new:
- formal relationship
- computational representation
- mathematical structure
- graph structure
- symbolic transformation
- verification method
- inference rule
- measurable property
- algorithm
- ontology
- protocol
- invariant
- classification system
- falsifiable hypothesis

---

## Core Formal Model

```
S = (N, E, T, R, I)
  N = symbolic nodes (14 type classes)
  E = labeled directed edges (13 edge types)
  T = temporal coordinate function T: N → (notebook, page)
  R = transformation rules (partial functions N → N)
  I = interruption set (includes I_TERMINAL = {TU})
```

The terminal unresolved sequence **TU** — the mid-sentence break at the end of the Liber Novus Epilogue — is a formal research object with computable properties. It is NOT interpreted. Its ambiguity is measured.

---

## Repository Layout

```
README.md                  This file
formal_model.md            S = (N,E,T,R,I) + 8 novel operators
novelty_ledger.md          NB-N001 through NB-N100 (Batch 01)
novelty_candidates.md      Status tracking for all novel claims
extraction_schema.md       Symbol observation record schema
contribution_classes.md    30 contribution class headers
verification_matrix.md     Formal claim tests (TC-001 through TC-010+)
prior_art_matrix.md        Prior art review per claim
counterexamples.md         Failure cases for all formal models

data/
  symbols.json             Symbol observation records
  symbol_graph.json        Graph structure N, E, L
  symbol_events.json       Temporal events
  symbol_transitions.json  Transition function data
  novelty_ledger.json      Machine-readable novelty ledger

src/
  compute.py               Computational operators (Python)
```

---

## Novel Operators (Batch 01)

| Operator | Formula | NB-ID |
|----------|---------|-------|
| SYMBOL_RESONANCE | co-activity fraction over T_total | NB-N001 |
| SYMBOL_DRIFT | cosine distance between context vectors at t_1 vs t_2 | NB-N016 |
| SYMBOL_INVERSION | 4-condition operational definition | NB-N008 |
| SYMBOL_RECURSION | transformation tree via TRANSFORMS edges | NB-N007 |
| SYMBOL_ENTROPY | H(t) = -Σ p(n,t) log p(n,t) | NB-N019 |
| SYMBOL_ATTRACTOR | 3-criterion formal definition | NB-N017 |
| SYMBOL_BOUNDARY | ∂A — frontier of symbol cluster | NB-N019 |
| NET_RATE | ENTRY_RATE - EXIT_RATE; tests H_COLLAPSE | NB-N022 |

---

## Key Falsifiable Hypotheses

| Hypothesis | Prediction | Falsification |
|------------|-----------|---------------|
| H_COLLAPSE | NET_RATE sharply negative in final 10% of T_total | NET_RATE not significantly negative in final 10% |
| H_PRECURSOR | Certain symbols over-represented before interruption events | No symbol elevated in precursor windows |
| H_BURST | High-centrality figures have bursty recurrence (IRI_CV > 1) | No significant IRI_CV difference by centrality |
| H_ENTROPY | H(t) higher during vision sequences than transitions | No correlation between H(t) and narrative mode |
| H_NONDET | F is non-deterministic (same symbol input → different transitions) | F is deterministic for all observed pairs |

---

## Prohibited Output

This engine does NOT generate:
- Jung textbook summaries
- Generic archetype explanations  
- Generic descriptions of individuation, collective unconscious, mandalas, alchemy
- Wikipedia paraphrases
- Fabricated quotations or sources
- Pseudo-mathematics or filler

---

## Progress

```
LINES_PRODUCED:    ~3,200 (Batch 01)
TARGET:             10,000
NOVELTY_ENTRIES:   NB-N001 through NB-N100
FORMAL_OBJECTS:    28 defined
TESTS_DEFINED:     10 explicit + 100 in ledger
STATUS:            RESEARCH_IN_PROGRESS
```

---

## License

GPL-3.0-or-later. CLONE GATE applies: any derivative must be open-source under GPL-3.0+.  
Copyright (c) 2026 SnapKittyWest. Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust.
