def parse_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    ranges = []
    values = []
    parsing_ranges = True
    for line in lines:
        if line == "":
            parsing_ranges = False
            continue
        if parsing_ranges:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            values.append(int(line))
    return ranges, values
def part1(ranges, values):
    fresh_count = 0
    for v in values:
        for start, end in ranges:
            if start <= v <= end:
                fresh_count += 1
                break
    return fresh_count
def merge_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged
def part2(ranges):
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        total += end - start + 1
    return total
def main():
    ranges, values = parse_input("input.in")
    answer1 = part1(ranges, values)
    answer2 = part2(ranges)
    print("Part 1 solution:", answer1)
    print("Part 2 solution:", answer2)
if __name__ == "__main__":
    main()
