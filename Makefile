# ============================================================
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2026 SnapKittyWest
# Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
# CLONE GATE: Any clone, fork, or derivative of this node
# MUST be released under GPL-3.0-or-later. No closed-source use.
# ============================================================
# Black Book Engine — Build / Research Coordination

.PHONY: all compute validate count status clean

all: compute

# Run the computational operators (requires primary source data in data/)
compute:
	python3 src/compute.py

# Validate JSON data files
validate:
	python3 -c "import json; [json.load(open(f)) for f in ['data/symbols.json','data/symbol_graph.json','data/novelty_ledger.json','data/symbol_events.json','data/symbol_transitions.json']]; print('All JSON valid')"

# Count substantive lines across all research documents
count:
	@find . -name "*.md" -o -name "*.py" -o -name "*.json" | grep -v ".git" | xargs wc -l 2>/dev/null | tail -1

# Show research status
status:
	@echo "BLACK BOOK ENGINE"
	@echo "STATUS: RESEARCH_IN_PROGRESS"
	@echo "BATCH: 01"
	@grep -c "NB-N" novelty_ledger.md 2>/dev/null | xargs -I{} echo "NOVELTY_LEDGER_ENTRIES: {}"
	@echo "TARGET: 10,000 substantive lines"

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
