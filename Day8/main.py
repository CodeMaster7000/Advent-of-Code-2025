import math
from itertools import combinations
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True
points = []
with open("input.in") as f:
    for line in f:
        x, y, z = map(int, line.strip().split(","))
        points.append((x, y, z))
n = len(points)
edges = []
for (i, p1), (j, p2) in combinations(enumerate(points), 2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    dist = dx*dx + dy*dy + dz*dz
    edges.append((dist, i, j))
edges.sort(key=lambda e: e[0])
uf1 = UnionFind(n)
connections = 0
for _, i, j in edges:
    if connections == 1000:
        break
    if uf1.union(i, j):
        connections += 1
component_sizes = {}
for i in range(n):
    root = uf1.find(i)
    component_sizes[root] = component_sizes.get(root, 0) + 1
largest_three = sorted(component_sizes.values(), reverse=True)[:3]
part1_answer = largest_three[0] * largest_three[1] * largest_three[2]
print("Part 1 solution:", part1_answer)
uf2 = UnionFind(n)
for _, i, j in edges:
    if uf2.union(i, j):
        if uf2.components == 1:
            x1 = points[i][0]
            x2 = points[j][0]
            part2_answer = x1 * x2
            break
print("Part 2 solution:", part2_answer)
