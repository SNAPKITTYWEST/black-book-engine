# ============================================================
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2026 SnapKittyWest
# Ahmad Ali Parr / Bel Esprit D'Accord Irrevocable Trust
# CLONE GATE: Any clone, fork, or derivative of this node
# MUST be released under GPL-3.0-or-later. No closed-source use.
# ============================================================
"""
Black Book Engine — Computational Operators
Implements the formal operators defined in formal_model.md

STATUS: RESEARCH_IN_PROGRESS
All functions are stubs pending primary source data.
"""

import math
import json
from typing import Dict, List, Optional, Set, Tuple


# ── Type aliases ──────────────────────────────────────────────
NodeID = str        # SID from symbols.json
Time = Tuple[int, int]  # (notebook, page)
EdgeLabel = str     # element of L


# ── Core data classes ─────────────────────────────────────────
class SymbolicNode:
    """A node n ∈ N in the symbolic state system S = (N, E, T, R, I)."""
    def __init__(self, sid: NodeID, symbol_text: str,
                 t_first: Optional[Time] = None,
                 t_last: Optional[Time] = None,
                 type_classes: Optional[List[str]] = None):
        self.sid = sid
        self.symbol_text = symbol_text
        self.t_first = t_first
        self.t_last = t_last
        self.type_classes = type_classes or []
        self.interruption_flag = False

    @property
    def t_span(self) -> Optional[int]:
        """T_span(n) = T_last - T_first in page units."""
        if self.t_first is None or self.t_last is None:
            return None
        k1, j1 = self.t_first
        k2, j2 = self.t_last
        # Simplified: assume 100 pages per notebook
        return (k2 * 100 + j2) - (k1 * 100 + j1)


class SymbolicGraph:
    """G = (N, E) — the Black Book symbol graph."""
    def __init__(self):
        self.nodes: Dict[NodeID, SymbolicNode] = {}
        self.edges: List[Tuple[NodeID, NodeID, EdgeLabel]] = []
        self.interruption_set: Set[NodeID] = set()

    def add_node(self, node: SymbolicNode):
        self.nodes[node.sid] = node

    def add_edge(self, from_id: NodeID, to_id: NodeID, label: EdgeLabel):
        self.edges.append((from_id, to_id, label))

    def neighbors(self, nid: NodeID) -> List[NodeID]:
        return [b for (a, b, _) in self.edges if a == nid]

    def degree(self, nid: NodeID) -> int:
        return sum(1 for (a, b, _) in self.edges if a == nid or b == nid)


# ── SYMBOL_RESONANCE ──────────────────────────────────────────
def resonance(a: SymbolicNode, b: SymbolicNode, t_total: int) -> float:
    """
    RESONANCE(a, b) = fraction of T_total during which both a and b are active.

    NOVEL_CANDIDATE: NB-N001 variant
    CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT
    """
    if a.t_first is None or b.t_first is None:
        return 0.0
    if t_total == 0:
        return 0.0
    # Overlap interval
    a_start = a.t_first[0] * 100 + a.t_first[1]
    a_end   = a.t_last[0] * 100 + a.t_last[1] if a.t_last else t_total
    b_start = b.t_first[0] * 100 + b.t_first[1]
    b_end   = b.t_last[0] * 100 + b.t_last[1] if b.t_last else t_total
    overlap = max(0, min(a_end, b_end) - max(a_start, b_start))
    return overlap / t_total


# ── SYMBOL_DRIFT ─────────────────────────────────────────────
def symbol_drift(node: SymbolicNode,
                 context_t1: Dict[NodeID, int],
                 context_t2: Dict[NodeID, int]) -> float:
    """
    DRIFT(n, t_1, t_2) = cosine distance between context vectors at t_1 and t_2.

    NOVEL_CANDIDATE: NB-N016
    CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT, NEW_MEASUREMENT
    """
    all_keys = set(context_t1.keys()) | set(context_t2.keys())
    v1 = [context_t1.get(k, 0) for k in all_keys]
    v2 = [context_t2.get(k, 0) for k in all_keys]
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(x**2 for x in v1))
    mag2 = math.sqrt(sum(x**2 for x in v2))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    cosine_sim = dot / (mag1 * mag2)
    return 1.0 - cosine_sim  # cosine distance


# ── SYMBOL_ENTROPY ────────────────────────────────────────────
def symbolic_entropy(active_nodes: List[SymbolicNode], t: int) -> float:
    """
    H(t) = -Σ p(n,t) log p(n,t) for all active nodes at time t.

    NOVEL_CANDIDATE: NB-N019
    CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT, NEW_MEASUREMENT
    RESEARCH HYPOTHESIS: High H(t) → imaginal complexity peak (NOT established fact)
    """
    active = [n for n in active_nodes
              if n.t_first is not None
              and n.t_first[0] * 100 + n.t_first[1] <= t
              and (n.t_last is None or n.t_last[0] * 100 + n.t_last[1] >= t)]
    if not active:
        return 0.0
    p = 1.0 / len(active)
    return -len(active) * p * math.log(p) if p > 0 else 0.0


# ── SYMBOL_RECURSION ─────────────────────────────────────────
def symbol_recursion(graph: SymbolicGraph, nid: NodeID, depth: int) -> Set[NodeID]:
    """
    RECURSION(n, d) — transformation tree up to depth d.

    NOVEL_CANDIDATE: NB-N007
    CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT
    """
    if depth == 0:
        return {nid}
    result = {nid}
    for (a, b, label) in graph.edges:
        if a == nid and label == 'TRANSFORMS':
            result |= symbol_recursion(graph, b, depth - 1)
    return result


def recursion_depth(graph: SymbolicGraph, nid: NodeID, max_depth: int = 20) -> int:
    """RECURSION_DEPTH(n) = max d such that RECURSION(n,d) ≠ RECURSION(n,d-1)."""
    prev = symbol_recursion(graph, nid, 0)
    for d in range(1, max_depth + 1):
        curr = symbol_recursion(graph, nid, d)
        if curr == prev:
            return d - 1
        prev = curr
    return max_depth


# ── INTERRUPTION_DENSITY ─────────────────────────────────────
def interruption_density(interruptions: List[int], t1: int, t2: int) -> float:
    """
    INTERRUPTION_DENSITY(t1, t2) = |I ∩ [t1, t2]| / (t2 - t1).

    NOVEL_CANDIDATE: NB-N015
    CONTRIBUTION_TYPE: NEW_MATHEMATICAL_OBJECT, NEW_MEASUREMENT
    """
    if t2 <= t1:
        return 0.0
    count = sum(1 for i in interruptions if t1 <= i <= t2)
    return count / (t2 - t1)


# ── NET_RATE ──────────────────────────────────────────────────
def net_rate(nodes: List[SymbolicNode], t: int, k: int) -> float:
    """
    NET_RATE(t, k) = ENTRY_RATE(t,k) - EXIT_RATE(t,k).
    NET_RATE > 0 → symbolic expansion
    NET_RATE < 0 → symbolic contraction

    RESEARCH HYPOTHESIS H_COLLAPSE: NET_RATE sharply negative approaching terminal interruption.
    FALSIFICATION: NET_RATE not significantly negative in final 10% of T_total.
    """
    if k == 0:
        return 0.0
    entries = sum(1 for n in nodes
                  if n.t_first is not None
                  and t <= n.t_first[0] * 100 + n.t_first[1] < t + k)
    exits   = sum(1 for n in nodes
                  if n.t_last is not None
                  and t <= n.t_last[0] * 100 + n.t_last[1] < t + k)
    return (entries - exits) / k


# ── REAPPEARANCE_LAG ─────────────────────────────────────────
def reappearance_lag(appearances: List[int], gap_threshold: int = 10) -> Optional[int]:
    """
    REAPPEARANCE_LAG(n): time from last appearance before a gap to first appearance after.
    Returns None if no reappearance detected.

    NOVEL_CANDIDATE: NB-N010
    """
    if len(appearances) < 2:
        return None
    appearances = sorted(appearances)
    for i in range(len(appearances) - 1):
        gap = appearances[i + 1] - appearances[i]
        if gap > gap_threshold:
            return gap
    return None


# ── LOAD_GRAPH ────────────────────────────────────────────────
def load_graph(symbols_path: str, graph_path: str) -> SymbolicGraph:
    """Load symbol graph from JSON files."""
    with open(symbols_path) as f:
        sym_data = json.load(f)
    with open(graph_path) as f:
        graph_data = json.load(f)

    g = SymbolicGraph()
    for rec in sym_data.get('records', []):
        node = SymbolicNode(
            sid=rec['SID'],
            symbol_text=rec['SYMBOL_TEXT'],
            type_classes=rec.get('TYPE_CLASS', [])
        )
        node.interruption_flag = rec.get('INTERRUPTION_FLAG', False)
        g.add_node(node)
        if node.interruption_flag:
            g.interruption_set.add(node.sid)

    for edge in graph_data.get('edges', []):
        g.add_edge(edge['from'], edge['to'], edge['label'])

    return g


if __name__ == '__main__':
    print("Black Book Engine — compute.py")
    print("STATUS: RESEARCH_IN_PROGRESS")
    print("All operators defined. Primary source data required to execute.")
    print()
    print("Defined operators:")
    print("  resonance(a, b, t_total)")
    print("  symbol_drift(node, context_t1, context_t2)")
    print("  symbolic_entropy(active_nodes, t)")
    print("  symbol_recursion(graph, nid, depth)")
    print("  recursion_depth(graph, nid)")
    print("  interruption_density(interruptions, t1, t2)")
    print("  net_rate(nodes, t, k)")
    print("  reappearance_lag(appearances, gap_threshold)")
