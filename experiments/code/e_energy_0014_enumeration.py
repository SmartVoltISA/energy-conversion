"""Reproducibility script for E-ENERGY-0014.

Enumerates all connected undirected simple graphs on 4 labeled nodes,
with maximum degree <= 3, and verifies the reported state/transition counts.

Model: one legal elementary transition toggles exactly one edge while
preserving the admissibility constraints.
"""
from itertools import combinations
from collections import deque

N = 4
EDGES = list(combinations(range(N), 2))


def degrees(mask):
    d = [0] * N
    for i, (u, v) in enumerate(EDGES):
        if mask & (1 << i):
            d[u] += 1
            d[v] += 1
    return d


def connected(mask):
    if mask == 0:
        return False
    seen = {0}
    changed = True
    while changed:
        changed = False
        for i, (u, v) in enumerate(EDGES):
            if mask & (1 << i):
                if u in seen and v not in seen:
                    seen.add(v); changed = True
                elif v in seen and u not in seen:
                    seen.add(u); changed = True
    return len(seen) == N


def admissible(mask):
    return connected(mask) and max(degrees(mask)) <= 3

states = [m for m in range(1 << len(EDGES)) if admissible(m)]
state_set = set(states)

neighbors = {m: set() for m in states}
for m in states:
    for i in range(len(EDGES)):
        q = m ^ (1 << i)
        if q in state_set:
            neighbors[m].add(q)

transition_count = sum(len(v) for v in neighbors.values()) // 2
P = [len(neighbors[m]) for m in states]

# Verify shortest-path symmetry of the transition graph.
for start in states:
    dist = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in neighbors[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert len(dist) == len(states), "Admissible transition graph is disconnected"
    for target, d in dist.items():
        reverse_dist = {target: 0}
        q = deque([target])
        while q:
            u = q.popleft()
            for v in neighbors[u]:
                if v not in reverse_dist:
                    reverse_dist[v] = reverse_dist[u] + 1
                    q.append(v)
        assert reverse_dist[start] == d

assert len(states) == 38, len(states)
assert transition_count == 84, transition_count
assert min(P) == 3, min(P)
assert max(P) == 6, max(P)

print("E-ENERGY-0014 reproduction: PASS")
print(f"admissible states = {len(states)}")
print(f"undirected one-step transitions = {transition_count}")
print(f"local P range = {min(P)}..{max(P)}")
print("shortest-path symmetry = PASS")
