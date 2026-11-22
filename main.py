from collections import deque

def topo_sort(nodes, edges):
    adj = {u: [] for u in nodes}; indeg = {u: 0 for u in nodes}
    for u, v in edges: adj[u].append(v); indeg[v] += 1
    q = deque([u for u in nodes if indeg[u] == 0]); order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
    if len(order) != len(nodes): raise ValueError("Cycle detected")
    return order

if __name__ == "__main__":
    assert topo_sort(["compile", "test", "package"], [("compile", "test"), ("test", "package")]) == ["compile", "test", "package"]
    print("[PASS] 013_topological_dag_sort")
