"""Independent reproduction of E-ENERGY-0014.

Four labeled nodes; connected simple undirected graphs with max degree <= 3.
A legal transition toggles exactly one edge while preserving admissibility.
Expected: 38 states, 84 undirected one-step transitions, P range 3..6,
and symmetric shortest-path distances.
"""
from collections import deque
from itertools import combinations
N=4
EDGES=list(combinations(range(N),2))

def deg(m):
 d=[0]*N
 for i,(a,b) in enumerate(EDGES):
  if m>>i&1:d[a]+=1;d[b]+=1
 return d

def conn(m):
 adj=[[] for _ in range(N)]
 for i,(a,b) in enumerate(EDGES):
  if m>>i&1:adj[a].append(b);adj[b].append(a)
 seen={0};q=deque([0])
 while q:
  v=q.popleft()
  for w in adj[v]:
   if w not in seen:seen.add(w);q.append(w)
 return len(seen)==N

def ok(m): return conn(m) and max(deg(m))<=3

def nbr(m): return [m^(1<<i) for i in range(6) if ok(m^(1<<i))]

def bfs(s):
 d={s:0};q=deque([s])
 while q:
  v=q.popleft()
  for w in nbr(v):
   if w not in d:d[w]=d[v]+1;q.append(w)
 return d

def main():
 S=[m for m in range(64) if ok(m)]
 assert len(S)==38
 pairs={tuple(sorted((a,b))) for a in S for b in nbr(a)}
 assert len(pairs)==84
 p=[len(nbr(s)) for s in S]
 assert (min(p),max(p))==(3,6)
 D={s:bfs(s) for s in S}
 assert all(len(D[s])==38 for s in S)
 assert all(D[a][b]==D[b][a] for a in S for b in S)
 print('PASS: states=38 transitions=84 P=3..6 distance_symmetry=PASS')
if __name__=='__main__':main()
