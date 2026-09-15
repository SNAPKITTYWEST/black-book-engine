<!--
  SPDX-License-Identifier: GPL-3.0-or-later
  Copyright (c) 2026 SnapKittyWest
  Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
  CLONE GATE: Any clone, fork, or derivative of this node
  MUST be released under GPL-3.0-or-later. No closed-source use.
-->

# Symbol Extraction Schema — Black Book Engine

STATUS: RESEARCH_IN_PROGRESS  
PURPOSE: Enforce SOURCE/INFERENCE SEPARATION in all extraction operations

---

## SYMBOL_OBSERVATION_RECORD Schema

| Field | Type | Description |
|-------|------|-------------|
| SID | string | Unique symbol identifier (e.g., SYM-001) |
| SYMBOL_TEXT | string | Textual label as it appears in source |
| FIRST_OCCURRENCE | (int, int) | T_first in (notebook, page) coordinates |
| LAST_OCCURRENCE | (int, int) | T_last in (notebook, page) coordinates |
| SPAN | int | T_span = T_last - T_first |
| OCCURRENCE_COUNT | int | Total number of distinct appearances |
| TYPE_CLASS | list | One or more of: N_SYMBOL, N_FIGURE, N_OBJECT, N_PLACE, N_ACTION, N_COLOR, N_NUMBER, N_FORM, N_ANIMAL, N_ELEMENT, N_TEXT, N_DREAM, N_VISION, N_TEMPORAL |
| CONTEXT_SUMMARY | string | Brief description of contexts of appearance — NOT an interpretation; raw description |
| CO_OCCURRING_SIDs | list | Other SIDs appearing within w=5 pages of each occurrence |
| TRANSFORMATION_SIDs | list | SIDs this symbol is documented to transform into or from |
| OPPOSITION_SIDs | list | SIDs in OPPOSES relationship |
| MODE_FLAGS | enum | DREAM_MODE \| VISION_MODE \| BOTH |
| INTERRUPTION_FLAG | bool | TRUE if associated with interrupted sequence in I |
| INTERPRETATION_LOCK | const | Always LOCKED — no interpretive content in observation record |
| PROVENANCE | tuple | (notebook, page, section, mode) |
| CONFIDENCE | enum | HIGH \| MEDIUM \| LOW |
| VERIFIED_BY | string | Source cross-reference for CONFIDENCE = HIGH |

**RULE:** INTERPRETATION_LOCK = LOCKED on all SYMBOL_OBSERVATION_RECORDs.  
Interpretations are stored ONLY in HYPOTHESIS_REGISTER.

---

## HYPOTHESIS_REGISTER Schema

| Field | Type | Description |
|-------|------|-------------|
| HID | string | Unique hypothesis identifier (e.g., HYP-001) |
| RELATED_SIDs | list | Symbol IDs this hypothesis concerns |
| HYPOTHESIS_TEXT | string | Statement of the hypothesis |
| HYPOTHESIS_TYPE | enum | FORMAL_PROPERTY \| SEMANTIC_MAPPING \| TEMPORAL_CLAIM \| STRUCTURAL_CLAIM \| PSYCHOLOGICAL_INTERPRETATION |
| STATUS | enum | NOVEL_CANDIDATE \| NON_NOVEL \| PRIOR_ART_REVIEW_REQUIRED |
| TEST_METHOD | string | How the hypothesis could be verified |
| FAILURE_CONDITION | string | What would falsify this hypothesis |
| EXISTING_CONCEPT | string | If related to a known concept, reference here |
| DISTINCTION | string | Formal statement of how this hypothesis differs from existing concept |

---

## EXTRACTION_PROTOCOL

```
STEP 1: RAW_EXTRACTION
  - Read source material without applying interpretive frames
  - Record: symbol text, context, page, notebook
  - DO NOT assign Jungian category at this step
  - Assign only TYPE_CLASS (structural classification, not interpretive)

STEP 2: CO_OCCURRENCE_COMPUTATION
  - For each extracted symbol, find all other symbols within w=5 pages
  - Record CO_OCCURRING_SIDs
  - Mechanical operation — no interpretation required

STEP 3: EDGE_ASSIGNMENT
  - For each pair with documented relationships:
    Assign edge label from L = { PRECEDES, FOLLOWS, CONTAINS, TRANSFORMS,
    OPPOSES, MERGES, SEPARATES, REPEATS, DISAPPEARS, REAPPEARS,
    INTERRUPTS, RESOLVES, FAILS_TO_RESOLVE }
  - Only assign if EXPLICITLY ATTESTED in source
  - Mark inferred edges as INFERRED (lower confidence)

STEP 4: TEMPORAL_ORDERING
  - Order all symbols by T_first; assign T coordinates
  - Record T_span, OCCURRENCE_COUNT

STEP 5: INTERRUPTION_IDENTIFICATION
  - Flag all symbols and edges associated with unresolved or interrupted sequences
  - Assign INTERRUPTION_FLAG = TRUE
  - Add to I (interruption set)

STEP 6: HYPOTHESIS_GENERATION (separate from steps 1-5)
  - Only AFTER steps 1-5 are complete
  - Store in HYPOTHESIS_REGISTER, NOT in SYMBOL_OBSERVATION_RECORD
  - Enforces SOURCE/INFERENCE SEPARATION
```

---

## SOURCE/INFERENCE SEPARATION

Every statement MUST be classified as exactly one:

| Classification | Meaning |
|----------------|---------|
| SOURCE_FACT | Directly attested in primary source |
| SOURCE_OBSERVATION | Observed in source without interpretation |
| MODEL_INFERENCE | Derived from the formal model S |
| NEW_HYPOTHESIS | A proposed but untested claim |
| NEW_FORMALISM | A formal mathematical definition |
| NEW_ALGORITHM | A computational procedure |
| NEW_INVARIANT | A property claimed to be invariant |
| NEW_TEST | A verification procedure |
| UNVERIFIED_HYPOTHESIS | A hypothesis without completed test |

---

## PROHIBITED OPERATIONS

- DO NOT assign Jungian archetype labels in SYMBOL_OBSERVATION_RECORD
- DO NOT use "FIRST EVER", "UNIQUE", "NEVER BEFORE DISCOVERED" without prior art search
- DO NOT fabricate quotations or sources
- DO NOT present MODEL_INFERENCE as SOURCE_FACT
- DO NOT count non-novel contributions toward the 10,000-line requirement
- DO NOT generate Jung textbook summaries as research output

---

*STATUS: RESEARCH_IN_PROGRESS | Schema defined | Extraction pending primary source access*
