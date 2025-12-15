from collections import defaultdict
def read_input(filename):
    points = []
    with open(filename) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            points.append((x, y))
    return points
def part1(points):
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    return (max_x - min_x + 1) * (max_y - min_y + 1)
def build_edges(points):
    edges = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        edges.append((x1, y1, x2, y2))
    return edges
def fill_polygon(points):
    edges = build_edges(points)
    filled = set(points)
    for x1, y1, x2, y2 in edges:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                filled.add((x1, y))
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                filled.add((x, y1))
    intersections = defaultdict(list)
    for x1, y1, x2, y2 in edges:
        if x1 == x2:
            y_start, y_end = sorted((y1, y2))
            for y in range(y_start, y_end):
                intersections[y].append(x1)
    for y, xs in intersections.items():
        xs.sort()
        for i in range(0, len(xs), 2):
            x_start, x_end = xs[i], xs[i + 1]
            for x in range(x_start, x_end + 1):
                filled.add((x, y))
    return filled
def rectangle_is_valid(p1, p2, filled):
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax = sorted((x1, x2))
    ymin, ymax = sorted((y1, y2))
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if (x, y) not in filled:
                return False
    return True
def part2(points):
    filled = fill_polygon(points)
    red_set = set(points)
    best = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area <= best:
                continue
            if rectangle_is_valid((x1, y1), (x2, y2), filled):
                best = area
    return best
if __name__ == "__main__":
    points = read_input("input.in")
    print("Part 1 solution:", part1(points))
    print("Part 2 solution:", part2(points))
