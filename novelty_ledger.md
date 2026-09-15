<!--
  SPDX-License-Identifier: GPL-3.0-or-later
  Copyright (c) 2026 SnapKittyWest
  Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
  CLONE GATE: Any clone, fork, or derivative of this node
  MUST be released under GPL-3.0-or-later. No closed-source use.
-->

# Novelty Ledger — Black Book Engine

STATUS: RESEARCH_IN_PROGRESS  
ENTRIES: NB-N001 through NB-N100  
TARGET: NB-N001 through NB-N10000  

Each entry format:
```
ID | SOURCE | OBSERVATION | EXISTING_CONCEPT | NEW_OPERATION | NEW_RELATION
NOVELTY_CLAIM | POTENTIAL_PRIOR_ART | DISTINCTION | TEST | STATUS
```

---

## NB-N001
**ID:** NB-N001  
**SOURCE:** Black Books structural observation  
**OBSERVATION:** The Black Books span 7 notebooks over ~19 years (1913–1932); minimum temporal granularity is notebook-level for symbol tracking  
**EXISTING_CONCEPT:** Temporal analysis of texts exists in general narratology  
**NEW_OPERATION:** Defining T: N → ℕ² (notebook × page) as a formal coordinate system for symbolic events specific to this material  
**NEW_RELATION:** Lexicographic order on T provides total temporal ordering on first symbol appearances  
**NOVELTY_CLAIM:** The specific coordinate system T = (notebook_index, page_index) defined over the Black Books as primary data is new as a formal object  
**POTENTIAL_PRIOR_ART:** Diachronic corpus analysis; timeline annotation in digital humanities  
**DISTINCTION:** This is not a linguistic timeline; it tracks imaginal symbol states with partial order semantics and interruption states  
**TEST:** Verify T is well-defined for 50-symbol sample; verify lexicographic ordering consistent with known temporal sequence of entries  
**STATUS:** NOVEL_CANDIDATE

---

## NB-N002
**ID:** NB-N002  
**SOURCE:** Liber Novus Epilogue (editorial notes, Shamdasani)  
**OBSERVATION:** The Epilogue of Liber Novus breaks off mid-sentence around 1959  
**EXISTING_CONCEPT:** Unfinished texts are studied in literary theory; manuscript studies treats incomplete texts as objects of study  
**NEW_OPERATION:** Classifying TU (terminal unresolved sequence) as a formal object with computable properties (ambiguity measure, possible-continuation distribution, syntactic class)  
**NEW_RELATION:** TU is an element of I_TERMINAL ⊂ I ⊂ S; this embeds the interruption into the formal model S  
**NOVELTY_CLAIM:** Treating the specific terminal break of Liber Novus as a formal mathematical object with computable properties (rather than purely hermeneutic phenomenon) is new  
**POTENTIAL_PRIOR_ART:** Manuscript completion studies; computational linguistics work on sentence completion  
**DISTINCTION:** The novel operation is computing the ambiguity measure of TU and generating a constrained completion distribution without asserting authorial intent — a formal constraint not present in purely hermeneutic or philological treatments  
**TEST:** Count grammatically valid continuations of TU; measure semantic entropy of the continuation distribution  
**STATUS:** NOVEL_CANDIDATE

---

## NB-N003
**ID:** NB-N003  
**SOURCE:** Black Books content observation  
**OBSERVATION:** Philemon appears as a named figure in the Black Books dialogues  
**EXISTING_CONCEPT:** Philemon is discussed as a symbol of the "Wise Old Man" archetype in Jungian literature  
**NEW_OPERATION:** Treating Philemon as node n_Philemon ∈ N_FIGURE and computing T_first, T_last, T_span, RESONANCE with other nodes, SYMBOL_DRIFT across appearances  
**NEW_RELATION:** Computing ATTRACTOR_BASIN(n_Philemon) to determine which other symbols transform toward or through Philemon  
**NOVELTY_CLAIM:** The formal network properties of n_Philemon (centrality, resonance vector, attractor basin size) have not been computed as formal objects  
**POTENTIAL_PRIOR_ART:** Social network analysis of literary characters; character network analysis in digital humanities  
**DISTINCTION:** Embedding n_Philemon in full S = (N, E, T, R, I) and computing formal properties including transformation tree and attractor basin — not merely identifying it as a character  
**TEST:** Compute degree centrality of n_Philemon in E; compare to background figures; hypothesis: n_Philemon has significantly higher centrality than average  
**STATUS:** NOVEL_CANDIDATE

---

## NB-N004
**ID:** NB-N004  
**SOURCE:** Black Books observation  
**OBSERVATION:** Serpent/dragon figures appear recurrently in the imaginal sequences  
**EXISTING_CONCEPT:** Serpent as a symbol is catalogued in Jungian and general mythological literature  
**NEW_OPERATION:** Distinguishing TOKEN occurrences from TYPE (tracking whether each serpent appearance is the same entity or new instantiation); constructing TOKEN_SEQUENCE(SERPENT_TYPE)  
**NEW_RELATION:** TYPE_RECURRENCE vs TOKEN_RECURRENCE distinction applied to imaginal entities as formal classification  
**NOVELTY_CLAIM:** Formally distinguishing type-recurrence from token-recurrence for symbolic entities in an imaginal text is a new taxonomic operation  
**POTENTIAL_PRIOR_ART:** Type/token distinction is standard in linguistics; application to imaginal symbol tracking is proposed novel extension  
**DISTINCTION:** In linguistics, type/token applies to word forms; here it applies to imaginal entities with continuity of identity — requiring different operational criteria for identity  
**TEST:** Define IDENTITY_CRITERIA for serpent entities; apply to all serpent appearances; classify each as same-entity or new-entity; compute TYPE_COUNT and TOKEN_COUNT  
**STATUS:** NOVEL_CANDIDATE

---

## NB-N005 through NB-N030

| ID | KEY_OPERATION | NOVELTY_CLAIM | STATUS |
|----|---------------|---------------|--------|
| NB-N005 | CHAPTER_CROSSING(n) — symbol persistence across chapter boundaries | Quantifying chapter-boundary persistence as formal property of imaginal symbols | NOVEL_CANDIDATE |
| NB-N006 | NUMBER_CENTRALITY(k) — degree centrality of numerical symbol k | Computing graph-theoretic centrality of numerical symbols in the symbol graph | NOVEL_CANDIDATE |
| NB-N007 | TRANSFORMATION_MONOID M(R) = (R, ∘, id) | Studying the algebraic (monoid) structure of symbolic transformation rules | NOVEL_CANDIDATE |
| NB-N008 | OPPOSITION_SUBGRAPH G_opp bipartiteness test | Testing bipartiteness of the opposition subgraph as a formal claim | NOVEL_CANDIDATE |
| NB-N009 | RESONANCE_MATRIX spectral analysis | Applying spectral analysis to resonance matrix to identify structural symbol clusters | NOVEL_CANDIDATE |
| NB-N010 | REAPPEARANCE_LAG(n) = T_reappearance - T_disappearance | Formal measurement of reappearance lag for imaginal symbols | NOVEL_CANDIDATE |
| NB-N011 | STRONGLY_CONNECTED_COMPONENTS of transformation graph G_R | Applying SCC analysis to the transformation graph of an imaginal symbol system | NOVEL_CANDIDATE |
| NB-N012 | MODAL_TRANSFER(n) — symbol appearing in both DREAM and VISION contexts | Formalizing dream/vision modal partition and measuring cross-modal symbol transfer | NOVEL_CANDIDATE |
| NB-N013 | LABEL_SIGNATURE(n) — distribution over edge label types | Defining label signatures and using them to define structural similarity | NOVEL_CANDIDATE |
| NB-N014 | COLOR_CO_OCCURRENCE_MATRIX + CHROMATIC_CLUSTERING | Computing chromatic co-occurrence structure prior to and independent of alchemical interpretation | NOVEL_CANDIDATE |
| NB-N015 | INTERRUPTION_DENSITY(t₁,t₂) = \|I ∩ [t₁,t₂]\| / (t₂ - t₁) | Quantifying interruption density as a temporal metric | NOVEL_CANDIDATE |
| NB-N016 | DIALOGUE_GRAPH — network of recurrent participatory events | Formal network analysis of dialogue sessions as a graph | NOVEL_CANDIDATE |
| NB-N017 | LANGUAGE L(TSA) recognized by the symbolic automaton | Characterizing symbolic dynamics as a formal language and testing its complexity class | NOVEL_CANDIDATE |
| NB-N018 | NAME_CENTRALITY_HYPOTHESIS — named figures have higher degree centrality | Testing naming-centrality hypothesis as a formal testable proposition | NOVEL_CANDIDATE |
| NB-N019 | SYMBOLIC_MARKOV_ENTROPY H_k and EXCESS_ENTROPY(k) | Computing Markov-order conditional entropy for symbolic imaginal sequences | NOVEL_CANDIDATE |
| NB-N020 | TOPOLOGICAL_INVARIANT_PRESERVATION under geometric symbol transformations | Testing topological invariant preservation under symbolic transformations | NOVEL_CANDIDATE |
| NB-N021 | KOLMOGOROV_COMPLEXITY_ESTIMATE via compression ratio | Computing symbolic compressibility as formal information-theoretic property | NOVEL_CANDIDATE |
| NB-N022 | EXTERNAL_COUPLING_COEFFICIENT — correlation between external events and H(t) | Computing formal coupling between historical events and local symbolic entropy | NOVEL_CANDIDATE |
| NB-N023 | CHROMATIC_NUMBER χ(G) of the symbol graph | Computing chromatic number as formal mathematical property of the symbol graph | NOVEL_CANDIDATE |
| NB-N024 | SELF_REFERENTIAL(n) — self-loop detection | Formally identifying self-referential imaginal symbols as distinct sub-population | NOVEL_CANDIDATE |
| NB-N025 | TIME_VARYING_R(t) — transformation rules as time-varying objects | Treating transformation rules as time-varying objects with stability metrics | NOVEL_CANDIDATE |
| NB-N026 | MEDIATION_SCORE(n) = H(CLUSTER_A) - H(CLUSTER_B) | Defining symbolic mediation in terms of entropy differential between connected clusters | NOVEL_CANDIDATE |
| NB-N027 | ELEMENTAL_SIGNATURE(n) — normalized distribution over N_ELEMENT co-occurrences | Computing elemental signatures as formal vectors; measuring elemental similarity | NOVEL_CANDIDATE |
| NB-N028 | HOMOLOGY of clique complex Δ(G); BETTI_NUMBERS β_0, β_1, β_2 | Computing persistent homology of the clique complex of the Black Books symbol graph | NOVEL_CANDIDATE |
| NB-N029 | INTERRUPTION_RATE(R_i) = fraction of R_i executions leading to interrupted state | Computing transformation completion rates quantifying resolution vs interruption frequency | NOVEL_CANDIDATE |
| NB-N030 | PROVENANCE_TABLE for all symbolic claims | Building formal provenance table for all symbolic claims in the research framework | NOVEL_CANDIDATE |

---

## NB-N031 through NB-N100 (Compact Entries)

| ID | KEY_OPERATION | STATUS |
|----|---------------|--------|
| NB-N031 | SYMBOL_FRAGMENTATION — edge-splitting analysis detecting single→multiple entity transitions | NOVEL_CANDIDATE |
| NB-N032 | SYMBOL_CONJUNCTION — edge-merging analysis detecting two entities merging into one | NOVEL_CANDIDATE |
| NB-N033 | SYMBOL_SUPPRESSION_INTERVAL — contiguous absence distinguishable from final disappearance | NOVEL_CANDIDATE |
| NB-N034 | SYMBOL_REAPPEARANCE_VELOCITY = 1 / REAPPEARANCE_LAG | NOVEL_CANDIDATE |
| NB-N035 | SYMBOL_CO_DISAPPEARANCE — correlated disappearance within w time units | NOVEL_CANDIDATE |
| NB-N036 | SYMBOL_CO_APPEARANCE — correlated first appearance within w time units | NOVEL_CANDIDATE |
| NB-N037 | GRAPH_DIAMETER — testing small-world property of the symbol graph | NOVEL_CANDIDATE |
| NB-N038 | CLUSTERING_COEFFICIENT(n) — local symbolic clustering | NOVEL_CANDIDATE |
| NB-N039 | GLOBAL_CLUSTERING(G) — vs random graph baseline | NOVEL_CANDIDATE |
| NB-N040 | POWER_LAW_TEST(G) — degree distribution analysis | NOVEL_CANDIDATE |
| NB-N041 | SYMBOL_AGE(n) = T_total - T_first(n); age vs centrality correlation | NOVEL_CANDIDATE |
| NB-N042 | TEMPORAL_DENSITY(t, w) — distinct active symbols per unit time | NOVEL_CANDIDATE |
| NB-N043 | PEAK_DENSITY_TIME = argmax_t TEMPORAL_DENSITY | NOVEL_CANDIDATE |
| NB-N044 | SYMBOL_PATH_LENGTH — graph connectivity test | NOVEL_CANDIDATE |
| NB-N045 | NULL_MODEL_COMPARISON vs Erdős-Rényi random graph | NOVEL_CANDIDATE |
| NB-N046 | MODULARITY(G, partition) — community structure | NOVEL_CANDIDATE |
| NB-N047 | INFOMAP_CLUSTERS — information-flow-based clustering | NOVEL_CANDIDATE |
| NB-N048 | MUTUAL_INFORMATION(n, m) — statistical dependence beyond co-occurrence | NOVEL_CANDIDATE |
| NB-N049 | TRANSFER_ENTROPY(n → m) — directed information flow | NOVEL_CANDIDATE |
| NB-N050 | GRANGER_CAUSALITY_TEST(n, m) — predictive symbolic relationships | NOVEL_CANDIDATE |
| NB-N051 | SYMBOL_PHASE_PORTRAIT — T_span vs degree scatter | NOVEL_CANDIDATE |
| NB-N052 | SYMBOLIC_BIFURCATION_POINT — qualitative structural change detection | NOVEL_CANDIDATE |
| NB-N053 | PRE_POST_BIFURCATION_COMPARISON | NOVEL_CANDIDATE |
| NB-N054 | SYMBOL_RESILIENCE — robustness after simulated deletion | NOVEL_CANDIDATE |
| NB-N055 | CRITICAL_SYMBOLS — deletion increases diameter by > threshold | NOVEL_CANDIDATE |
| NB-N056 | SYMBOLIC_MOTIF_COUNT — 3-node subgraph over-representation | NOVEL_CANDIDATE |
| NB-N057 | FEED_FORWARD_LOOP_COUNT in transformation graph G_R | NOVEL_CANDIDATE |
| NB-N058 | SYMBOL_PRODUCTION_RATE(t) | NOVEL_CANDIDATE |
| NB-N059 | SYMBOL_EXTINCTION_RATE(t) | NOVEL_CANDIDATE |
| NB-N060 | NET_SYMBOL_ACCUMULATION(t) | NOVEL_CANDIDATE |
| NB-N061 | SYMBOLIC_STEADY_STATE — equilibrium point | NOVEL_CANDIDATE |
| NB-N062 | PRE_INTERRUPTION_SYMBOL_COUNT at T_terminal - ε | NOVEL_CANDIDATE |
| NB-N063 | ACTIVE_AT_TERMINAL — symbols alive at moment of terminal interruption | NOVEL_CANDIDATE |
| NB-N064 | TERMINAL_ORPHAN_SYMBOLS — active symbols with unresolved edges at TU | NOVEL_CANDIDATE |
| NB-N065 | INTERRUPTION_INCOMPLETENESS_MEASURE = \|TERMINAL_ORPHANS\| / \|ACTIVE_AT_TERMINAL\| | NOVEL_CANDIDATE |
| NB-N066 | COMPLETION_PROBABILITY_DISTRIBUTION over TU | NOVEL_CANDIDATE |
| NB-N067 | SEMANTIC_COMPLETION_CLASS — classification of TU continuations | NOVEL_CANDIDATE |
| NB-N068 | TU_MINIMUM_DESCRIPTION_LENGTH — shortest valid continuation | NOVEL_CANDIDATE |
| NB-N069 | TU_SYNTACTIC_AMBIGUITY_INDEX = log \|TU_POSSIBLE_CONTINUATIONS\| | NOVEL_CANDIDATE |
| NB-N070 | TU_RESOLUTION_TYPES = {AFFIRMATION, NEGATION, CONTINUATION, CLOSURE, QUESTION, SUSPENSION} | NOVEL_CANDIDATE |
| NB-N071 | SYMBOL_SEQUENCE_SUFFIX_ARRAY | NOVEL_CANDIDATE |
| NB-N072 | SYMBOLIC_N_GRAM_DISTRIBUTION | NOVEL_CANDIDATE |
| NB-N073 | SYMBOL_LONGEST_COMMON_SUBSEQUENCE(v1, v2) | NOVEL_CANDIDATE |
| NB-N074 | VISION_EPISODE_DISTANCE_MATRIX | NOVEL_CANDIDATE |
| NB-N075 | FIGURE_PRESENCE_VECTOR(n) | NOVEL_CANDIDATE |
| NB-N076 | PRESENCE_CORRELATION_MATRIX | NOVEL_CANDIDATE |
| NB-N077 | LAGGED_CORRELATION(n, m, lag) | NOVEL_CANDIDATE |
| NB-N078 | MAXIMUM_LAG_PREDICTOR(n) | NOVEL_CANDIDATE |
| NB-N079 | SYMBOLIC_AUTOCORRELATION(n) | NOVEL_CANDIDATE |
| NB-N080 | SYMBOLIC_PERIODICITY_TEST | NOVEL_CANDIDATE |
| NB-N081 | RECURRENCE_QUANTIFICATION_ANALYSIS | NOVEL_CANDIDATE |
| NB-N082 | RECURRENCE_PLOT_VISUAL | NOVEL_CANDIDATE |
| NB-N083 | SYMBOL_LYAPUNOV_EXPONENT (heuristic) | NOVEL_CANDIDATE |
| NB-N084 | SYMBOLIC_COMPLEXITY_MEASURE C = H_k / H_0 * D | NOVEL_CANDIDATE |
| NB-N085 | SYMBOL_DIVERSITY_INDEX = H_0 / log \|N\| | NOVEL_CANDIDATE |
| NB-N086 | SYMBOL_EVENNESS | NOVEL_CANDIDATE |
| NB-N087 | DOMINANT_SYMBOL_FRACTION | NOVEL_CANDIDATE |
| NB-N088 | SYMBOL_RANK_FREQUENCY_LAW (Zipf test) | NOVEL_CANDIDATE |
| NB-N089 | SYMBOL_HEAPS_LAW (vocabulary growth test) | NOVEL_CANDIDATE |
| NB-N090 | CROSS_NOTEBOOK_SYMBOL_TURNOVER | NOVEL_CANDIDATE |
| NB-N091 | SYMBOL_JACCARD_SIMILARITY(k1, k2) | NOVEL_CANDIDATE |
| NB-N092 | NOTEBOOK_SYMBOL_NETWORK | NOVEL_CANDIDATE |
| NB-N093 | SYMBOL_EMERGENCE_RATE(k) | NOVEL_CANDIDATE |
| NB-N094 | SYMBOL_SURVIVAL_RATE(k) | NOVEL_CANDIDATE |
| NB-N095 | SYMBOLIC_ECOSYSTEM_MODEL | NOVEL_CANDIDATE |
| NB-N096 | SYMBOL_NICHE_OVERLAP | NOVEL_CANDIDATE |
| NB-N097 | COMPETITIVE_EXCLUSION_TEST | NOVEL_CANDIDATE |
| NB-N098 | SYMBOL_MUTUALISM_TEST | NOVEL_CANDIDATE |
| NB-N099 | KEYSTONE_SYMBOL_DETECTION | NOVEL_CANDIDATE |
| NB-N100 | SYMBOLIC_FOOD_WEB_STRUCTURE | NOVEL_CANDIDATE |

---

*NOVELTY_LEDGER_ENTRIES_CREATED: NB-N001 through NB-N100*  
*STATUS: RESEARCH_IN_PROGRESS*  
*NEXT: NB-N101 through NB-N500*
