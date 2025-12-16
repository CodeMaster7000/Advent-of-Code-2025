from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def parse_input(filename):
    graph = defaultdict(list)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            node, targets = line.split(": ")
            for t in targets.split():
                graph[node].append(t)
    return graph
def count_paths_you_to_out(graph):
    memo = {}
    def dfs(node):
        if node == "out":
            return 1
        if node in memo:
            return memo[node]
        total = 0
        for nxt in graph[node]:
            total += dfs(nxt)
        memo[node] = total
        return total
    return dfs("you")
def count_paths_svr_with_constraints(graph):
    memo = {}
    def dfs(node, seen_dac, seen_fft):
        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True
        if node == "out":
            return 1 if seen_dac and seen_fft else 0
        key = (node, seen_dac, seen_fft)
        if key in memo:
            return memo[key]
        total = 0
        for nxt in graph[node]:
            total += dfs(nxt, seen_dac, seen_fft)
        memo[key] = total
        return total
    return dfs("svr", False, False)
if __name__ == "__main__":
    graph = parse_input("input.in")
    part1 = count_paths_you_to_out(graph)
    part2 = count_paths_svr_with_constraints(graph)
    print("Part 1 solution:", part1)
    print("Part 2 solution:", part2)
