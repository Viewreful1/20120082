n,m,v = map(int,input().split())
adj = {}
for i in range(1,n+1):
    adj[i] = set()
for i in range(m):
    a,b = map(int,input().split())
    adj[a].add(b)
    adj[b].add(a)

# DFS
stack = [v]
visited = set()
while stack:
    cur = stack.pop()
    if cur in visited:
        continue
    print(cur, end=' ')
    visited.add(cur)
    for nextv in sorted(adj[cur],reverse=True):
        stack.append(nextv)
print()

# BFS
from queue import Queue
q = Queue()
q.put(v)
visited = set()
while not q.empty():
    cur = q.get()
    if cur in visited:
        continue
    print(cur, end=' ')
    visited.add(cur)
    for nextv in sorted(adj[cur]):
        q.put(nextv)