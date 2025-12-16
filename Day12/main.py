import re
def parse(path: str):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    shapes = {}
    i = 0
    while i < len(lines):
        ln = lines[i].strip()
        if not ln:
            i += 1
            continue
        m = re.fullmatch(r"(\d+):", ln)
        if m:
            idx = int(m.group(1))
            i += 1
            grid = []
            while i < len(lines) and lines[i].strip():
                grid.append(lines[i])
                i += 1
            shapes[idx] = grid
            continue
        if re.match(r"^\d+x\d+:", ln):
            break
        i += 1
    regions = []
    for j in range(i, len(lines)):
        ln = lines[j].strip()
        if not ln:
            continue
        m = re.fullmatch(r"(\d+)x(\d+):\s*(.*)", ln)
        if not m:
            continue
        w, h = int(m.group(1)), int(m.group(2))
        counts = [int(x) for x in m.group(3).split()] if m.group(3).strip() else []
        regions.append((w, h, counts))
    return shapes, regions
def solve(path: str) -> int:
    shapes, regions = parse(path)
    k = max(shapes) + 1 if shapes else 0
    hash_counts = [0] * k
    for idx, grid in shapes.items():
        hash_counts[idx] = sum(row.count("#") for row in grid)
    ans = 0
    for w, h, counts in regions:
        if len(counts) < k:
            counts = counts + [0] * (k - len(counts))
        needed = sum(counts[i] * hash_counts[i] for i in range(k))
        if needed <= w * h:
            ans += 1
    return ans
if __name__ == "__main__":
    out = solve("input.in")
    print(out)
    print("Merry Christmas everyone! 🎄 Happy coding 👨‍💻")
