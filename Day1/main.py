def read_input(filename="input.in"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]
def solve_part_1(rotations):
    dial = 50
    count = 0
    for move in rotations:
        direction = move[0]
        steps = int(move[1:])
        if direction == "R":
            dial = (dial + steps) % 100
        else:
            dial = (dial - steps) % 100
        if dial == 0:
            count += 1
    return count
def solve_part_2(rotations):
    dial = 50
    count = 0
    for move in rotations:
        direction = move[0]
        steps = int(move[1:])
        step_direction = 1 if direction == "R" else -1
        for _ in range(steps):
            dial = (dial + step_direction) % 100
            if dial == 0:
                count += 1
    return count
if __name__ == "__main__":
    rotations = read_input("input.in")
    part_1_answer = solve_part_1(rotations)
    part_2_answer = solve_part_2(rotations)
    print("Part 1 solution:", part_1_answer)
    print("Part 2 solution:", part_2_answer)
