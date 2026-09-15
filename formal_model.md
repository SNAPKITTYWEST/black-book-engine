<!--
  SPDX-License-Identifier: GPL-3.0-or-later
  Copyright (c) 2026 SnapKittyWest
  Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
  CLONE GATE: Any clone, fork, or derivative of this node
  MUST be released under GPL-3.0-or-later. No closed-source use.
-->

# Formal Model — Black Book Engine

STATUS: RESEARCH_IN_PROGRESS  
BATCH: 01  
CONTRIBUTION_TYPE: NEW_FORMALISM  

---

## Section 01 — Formal Model Foundation

### FORMAL_OBJECT: SYMBOLIC_STATE_SYSTEM

```
S = (N, E, T, R, I)
where:
  N = finite set of symbolic nodes
  E ⊆ N × N × L = set of labeled directed edges
  L = { PRECEDES, FOLLOWS, CONTAINS, TRANSFORMS, OPPOSES, MERGES,
        SEPARATES, REPEATS, DISAPPEARS, REAPPEARS, INTERRUPTS,
        RESOLVES, FAILS_TO_RESOLVE }
  T = (N ∪ E) → ℝ≥0, temporal assignment function
  R = set of transformation rules R_i : N → N (partial functions)
  I ⊆ N ∪ E = interruption set
```

SOURCE_BASIS: Model construction — no Jung source claims this structure  
CONTRIBUTION_TYPE: NEW_FORMALISM  
NOVELTY_STATUS: NOVEL_CANDIDATE  
VERIFICATION_METHOD: Check every observed symbol can be assigned a node in N; every relationship assigned an edge with label from L; T consistent with notebook temporal ordering; I correctly identifies all unresolved sequences  
FAILURE_CASE: If a symbol relationship cannot be labeled by any element of L, then L is incomplete and must be extended — detectable failure requiring L-expansion, not model failure  
DEPENDENCY: none

---

### FORMAL_OBJECT: SYMBOLIC_NODE_ONTOLOGY

N is partitioned into:

| Partition | Description |
|-----------|-------------|
| N_SYMBOL | recurring non-personal imaginal images |
| N_FIGURE | named or unnamed persons/entities in dialogues |
| N_OBJECT | physical or quasi-physical items |
| N_PLACE | locations (real, imaginal, architectural) |
| N_ACTION | events, verbs, processes observed in visions |
| N_COLOR | chromatic attributions |
| N_NUMBER | numerical occurrences (cardinal, ordinal, structural) |
| N_FORM | geometric shapes, spatial patterns |
| N_ANIMAL | zoomorphic entities |
| N_ELEMENT | classical or observed elemental forces |
| N_TEXT | textual units (speeches, passages) |
| N_DREAM | events marked as dream-mode |
| N_VISION | events marked as active imagination / vision-mode |
| N_TEMPORAL | named temporal references (years, seasons, phases) |

The partition is exhaustive: N = ∪ N_k  
The partition is NOT exclusive: a node may carry multiple type tags  

SOURCE_BASIS: Observation of the source material structure  
CONTRIBUTION_TYPE: NEW_FORMALISM (ontological partition)  
NOVELTY_STATUS: NOVEL_CANDIDATE  
VERIFICATION_METHOD: Apply partition to 100-node sample; verify each node receives at least one type assignment; verify no node requires a type outside the partition  
FAILURE_CASE: Existence of a node requiring a type not in the partition forces ONTOLOGY_EXTENSION_EVENT  
DEPENDENCY: SYMBOLIC_STATE_SYSTEM

---

### FORMAL_OBJECT: TEMPORAL_ASSIGNMENT_FUNCTION

```
Let BB = Black Books 1 through 7 (1913-1932)
T: N → ℕ²
T(n) = (k, j) where n first appears on page j of notebook k

Ordering: T(n_1) < T(n_2) iff k_1 < k_2, or (k_1 = k_2 and j_1 < j_2)

T_first(n) = earliest (k, j) pair for node n
T_last(n)  = latest (k, j) pair for node n
T_span(n)  = T_last(n) - T_first(n) = temporal persistence of n
```

SOURCE_BASIS: Black Books publication structure (7 notebooks)  
CONTRIBUTION_TYPE: NEW_FORMALISM (temporal coordinate system)  
NOVELTY_STATUS: NOVEL_CANDIDATE  
FAILURE_CASE: Symbol with ambiguous first appearance due to undated entry forces T(n) = UNDEFINED → recorded in TEMPORAL_AMBIGUITY_LOG  
DEPENDENCY: SYMBOLIC_STATE_SYSTEM

---

### FORMAL_OBJECT: SYMBOL_TRANSITION_FUNCTION

```
F: N × X → N
where X = set of observable textual/imaginal events

F(s, x) = s' means: given current symbolic state s and event x, next state is s'

Extended: F*(s, x_1 x_2 ... x_n) = s_n where s_0 = s and s_i = F(s_{i-1}, x_i)

DETERMINISTIC   if ∀ s ∈ N, ∀ x ∈ X: |{F(s,x)}| ≤ 1
NON_DETERMINISTIC if ∃ s ∈ N, x ∈ X: |{F(s,x)}| > 1
```

HYPOTHESIS (to be tested): F is non-deterministic in the Black Books  
FORMAL_CONSEQUENCE: if non-deterministic, model F as relation R ⊆ N × X × N  
NOVELTY_STATUS: NOVEL_CANDIDATE  
DEPENDENCY: SYMBOLIC_STATE_SYSTEM, TEMPORAL_ASSIGNMENT_FUNCTION

---

### FORMAL_OBJECT: INTERRUPTION_SET_DEFINITION

```
I ⊆ N ∪ E classified as:
  I_TEXT    = textual interruptions (sentences that break off)
  I_IMAGE   = imaginal sequences without resolution
  I_DIALOGUE = dialogues without formal closure
  I_TERMINAL = the final interruption at end of Epilogue (singleton)

I_TERMINAL = { TU } where TU = terminal unresolved sequence

TU properties:
  TU_GRAMMAR_CLASS          = syntactic class of TU
  TU_SEMANTIC_FIELD         = range of semantic fields consistent with TU
  TU_POSSIBLE_CONTINUATIONS = set of grammatically valid continuations
  TU_AMBIGUITY_MEASURE      = |TU_POSSIBLE_CONTINUATIONS| (or entropy)
```

CONSTRAINT: No element of TU_POSSIBLE_CONTINUATIONS shall be presented as intended completion  
SOURCE_BASIS: Liber Novus Epilogue breaks mid-sentence (Shamdasani editorial notes; Library of Congress records on 1959 completion attempt)  
CONTRIBUTION_TYPE: NEW_FORMALISM, NEW_OBJECT  
NOVELTY_STATUS: NOVEL_CANDIDATE  
DEPENDENCY: SYMBOLIC_STATE_SYSTEM

---

## Section 02 — Novel Symbolic Operators

### OPERATOR: SYMBOL_RESONANCE

```
RESONANCE(a, b) → ℝ≥0

RESONANCE(a, b) = |{ t : T(a) ≤ t ≤ T_last(a) AND T(b) ≤ t ≤ T_last(b) }| / T_total

RESONANCE(a, b) = 0 if symbols never co-occur in any temporal window
RESONANCE(a, b) = 1 if symbols co-occur across the entire text span
```

NOTE: This is NOT the Jungian concept of "resonance" (which is qualitative). This is an operationally defined co-occurrence measure.  
CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT, NEW_ALGORITHM  
NOVELTY_STATUS: NOVEL_CANDIDATE  
PRIOR_ART_CONCERN: general co-occurrence measures exist in corpus linguistics; novelty is application to temporal imaginal sequences with specific textual boundary conditions  
FAILURE_CASE: All symbol pairs have identical resonance → metric has no discriminative power  
DEPENDENCY: TEMPORAL_ASSIGNMENT_FUNCTION

---

### OPERATOR: SYMBOL_DRIFT

```
DRIFT(n, t_1, t_2) → context_vector_distance

CONTEXT(n, t) = multiset of symbols co-occurring with n within window w at t

DRIFT(n, t_1, t_2) = d( CONTEXT(n, t_1), CONTEXT(n, t_2) )
  where d = cosine distance on symbol frequency vectors

SEMANTIC_DRIFT(n) = max_{t_1, t_2} DRIFT(n, t_1, t_2)

DRIFT > threshold_stable → symbol has undergone contextual transformation
DRIFT ≤ threshold_stable → symbol is semantically stable
```

CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT, NEW_MEASUREMENT  
NOVELTY_STATUS: NOVEL_CANDIDATE  
FAILURE_CASE: No symbol shows DRIFT > threshold_stable → text is symbolically static (testable prediction)  
DEPENDENCY: TEMPORAL_ASSIGNMENT_FUNCTION, SYMBOL_RESONANCE

---

### OPERATOR: SYMBOL_INVERSION

```
INVERSION(n) → n'

n is INVERTED at time t if there exists n' ∈ N such that:
  (1) T(n') > T(n)
  (2) n' occupies a structurally opposing position to n in E
  (3) n' shares at least k contextual neighbors with n
  (4) n' is explicitly generated from n in the text or dialogue

PARTIAL_INVERSION: conditions (1), (2), (3) hold but (4) does not
  → relationship is hypothetical, must be marked UNVERIFIED_HYPOTHESIS
```

NOTE: INVERSION is NOT the same as Jungian "enantiodromia" (which is qualitative). INVERSION is operationally testable.  
CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT, NEW_DEFINITION  
NOVELTY_STATUS: NOVEL_CANDIDATE  
FAILURE_CASE: If condition (4) is never satisfied for any pair, INVERSION is an empty operator — falsifies claim that text contains formal symbolic inversions

---

### OPERATOR: SYMBOL_RECURSION

```
RECURSION(n, 0) = {n}
RECURSION(n, d) = {n} ∪ { RECURSION(m, d-1) : ∃ edge (n, m, TRANSFORMS) ∈ E }

RECURSION_DEPTH(n) = max d such that RECURSION(n, d) ≠ RECURSION(n, d-1)

RECURSIVELY_STABLE if RECURSION_DEPTH(n) = 0
RECURSIVELY_DEEP   if RECURSION_DEPTH(n) > threshold_deep
```

CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT  
NOVELTY_STATUS: NOVEL_CANDIDATE  
FAILURE_CASE: RECURSION_DEPTH(n) = 0 for all n → text contains no symbol transformations (falsifiable)

---

### OPERATOR: SYMBOL_ENTROPY

```
p(n | t) = 1 if T(n) ≤ t ≤ T_last(n), else 0
p(n, t)  = p(n | t) / Z(t)  where Z(t) = Σ_m p(m | t)

H(t)          = -Σ_n p(n,t) log p(n,t)     [local symbolic entropy at time t]
H_global      = (1/T_total) ∫ H(t) dt       [average symbolic entropy]
H_max         = log |N|                      [maximum possible entropy]
H_normalized(t) = H(t) / H_max
```

RESEARCH HYPOTHESIS: High H(t) → many symbols active simultaneously → imaginal complexity peak. This is HYPOTHESIS, not established fact.  
CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT, NEW_MEASUREMENT  
NOVELTY_STATUS: NOVEL_CANDIDATE  
FAILURE_CASE: H(t) shows no correlation with narrative complexity markers → entropy model has no explanatory power

---

### OPERATOR: SYMBOL_ATTRACTOR

```
Symbol n ∈ N is an ATTRACTOR if:
  (1) T_span(n) / T_total > threshold_persistent
  (2) RECURSION(n, 1) ⊇ {nodes that eventually transform to n}
  (3) RESONANCE(n, m) > threshold_resonance for multiple m ∈ N

ATTRACTOR_BASIN(n) = { m ∈ N : ∃ path through TRANSFORMS-edges reaching n }

REPELLOR: appears once, generates transformations away from itself, does not recur
```

CONTRIBUTION_TYPE: NEW_DEFINITION, NEW_MATHEMATICAL_OBJECT  
NOVELTY_STATUS: NOVEL_CANDIDATE  
FAILURE_CASE: No symbol satisfies all three criteria → no attractors exist in the model (testable)

---

### OPERATOR: SYMBOL_BOUNDARY

```
∂A = { n ∈ A : ∃ m ∉ A such that (n, m, ·) ∈ E or (m, n, ·) ∈ E }

BOUNDARY_DENSITY(A) = |∂A| / |A|

CLOSED cluster: ∂A = ∅  (no external connections)
OPEN   cluster: ∂A = A  (all nodes have external connections)
```

RESEARCH QUESTION: Are there closed symbol clusters in the Black Books? This would indicate isolated symbolic subsystems.  
CONTRIBUTION_TYPE: NEW_DEFINITION  
NOVELTY_STATUS: NOVEL_CANDIDATE  
FAILURE_CASE: No closed cluster exists → symbol graph is fully connected (itself a research finding)

---

## Section 05 — Temporal Dynamics Model

### TEMPORAL_STATE_MACHINE_DEFINITION

```
TSA = (N, X, F, s_0, ACC, I)
  N   = symbolic state space (nodes)
  X   = input event alphabet (textual/imaginal events)
  F   : N × X → 2^N (non-deterministic transition function)
  s_0 ∈ N = initial state
  ACC ⊆ N = accepting states (symbols associated with resolution)
  I   ⊆ N = interruption states (absorbing, non-accepting)

CRITICAL_INVARIANT: If s_t ∈ I then s_{t+k} = s_t for all k > 0
  (interruption is absorbing — models the terminal break)
```

### TEMPORAL_WINDOW_ANALYSIS

```
ACTIVE(t, k) = { n ∈ N : T_first(n) ≤ t ≤ T_last(n) and n appears in (t, t+k) }

ENTRY_RATE(t, k) = |{ n : T_first(n) ∈ (t, t+k) }| / k
EXIT_RATE(t, k)  = |{ n : T_last(n) ∈ (t, t+k) }| / k
NET_RATE(t, k)   = ENTRY_RATE(t, k) - EXIT_RATE(t, k)

NET_RATE > 0 → symbolic expansion
NET_RATE < 0 → symbolic contraction
NET_RATE ≈ 0 → symbolic equilibrium
```

RESEARCH HYPOTHESIS (H_COLLAPSE): The period approaching the terminal interruption is characterized by sharply negative NET_RATE.  
FALSIFICATION CONDITION: NET_RATE is not significantly negative in the final 10% of T_total.

---

## Section 06 — Interruption Theory

### INTERRUPTION_TAXONOMY

| Class | Description |
|-------|-------------|
| I_TEXT_MINOR | sentence breaks off; surrounding context continues |
| I_TEXT_MAJOR | section ends abruptly; next section is not continuation |
| I_DIALOGUE | dialogue sequence has no formal closure statement |
| I_IMAGE | visual/imaginal sequence not brought to resolution |
| I_PROGRAM | Jung explicitly states intention to continue but does not |
| I_TERMINAL | absolute terminal interruption (TU); unique singleton |

The six classes are exhaustive and mutually exclusive within a single event.

### TERMINAL_UNRESOLVED_SEQUENCE_FORMAL_OBJECT

```
TU = terminal unresolved clause of Liber Novus Epilogue

SOURCE_FACT: Epilogue breaks off mid-sentence
  (Shamdasani editorial apparatus; Library of Congress 1959 completion attempt records)

OPERATIONS ON TU:
  (1) SYNTACTIC_PARSE(TU_STRING)
  (2) CONTINUATION_SPACE(TU_STRING)
  (3) CONSTRAINED_CONTINUATION_SPACE:
        (a) grammatically well-formed
        (b) semantically coherent with preceding paragraphs
        (c) in the register and vocabulary of Liber Novus
  (4) AMBIGUITY_MEASURE = H(P) over CONSTRAINED_CONTINUATION_SPACE
  (5) DOMINANT_CONTINUATION = argmax P(s)
```

CONSTRAINT: DOMINANT_CONTINUATION must be labeled:  
`"COMPUTATIONALLY DERIVED MAXIMUM; NOT CLAIMED AS AUTHORIAL INTENT"`

---

*STATUS: RESEARCH_IN_PROGRESS | BATCH 01 | Lines ~1,200*
