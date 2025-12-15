def max_joltage(bank: str, k: int) -> int:
    stack = []
    to_remove = len(bank) - k
    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    return int("".join(stack[:k]))
def main():
    with open("input.in") as f:
        banks = f.read().strip().splitlines()
    part1 = sum(max_joltage(bank, 2) for bank in banks)
    part2 = sum(max_joltage(bank, 12) for bank in banks)
    print("Part 1 solution:", part1)
    print("Part 2 solution:", part2)
if __name__ == "__main__":
    main()
