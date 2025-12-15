from __future__ import annotations
import re
from dataclasses import dataclass
from typing import List, Tuple
LINE_RE = re.compile(
    r"^\s*\[(?P<diag>[.#]+)\](?P<buttons>(?:\s*\([^)]*\))+)\s*\{(?P<jolt>[^}]*)\}\s*$"
)
BTN_RE = re.compile(r"\(([^)]*)\)"
@dataclass
class Machine:
    diag: str
    buttons: List[Tuple[int, ...]]
    joltage: Tuple[int, ...]
def parse_input(path: str) -> List[Machine]:
    machines: List[Machine] = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            m = LINE_RE.match(line)
            if not m:
                raise ValueError(f"Bad line format: {raw!r}")
            diag = m.group("diag")
            btn_blob = m.group("buttons")
            jolt_blob = m.group("jolt").strip()
            buttons: List[Tuple[int, ...]] = []
            for b in BTN_RE.findall(btn_blob):
                b = b.strip()
                if b == "":
                    buttons.append(tuple())
                else:
                    buttons.append(tuple(int(x) for x in b.split(",")))

            joltage = tuple(int(x.strip()) for x in jolt_blob.split(",") if x.strip() != "")
            machines.append(Machine(diag=diag, buttons=buttons, joltage=joltage))
    return machines
def min_presses_part1(machine: Machine) -> int:
    n = len(machine.diag)
    target_mask = 0
    for i, ch in enumerate(machine.diag):
        if ch == "#":
            target_mask |= (1 << i)
    btn_masks: List[int] = []
    for btn in machine.buttons:
        mask = 0
        for idx in btn:
            if idx < 0 or idx >= n:
                raise ValueError("Button index out of range")
            mask ^= (1 << idx)
        btn_masks.append(mask)
    m = len(btn_masks)
    best = None
    for subset in range(1 << m):
        state = 0
        presses = 0
        for j in range(m):
            if (subset >> j) & 1:
                state ^= btn_masks[j]
                presses += 1
        if state == target_mask:
            if best is None or presses < best:
                best = presses
    if best is None:
        raise RuntimeError("No solution")
    return best
def min_presses_part2(machine: Machine) -> int:
    import pulp
    b = machine.joltage
    k = len(b)
    m = len(machine.buttons)
    affects = [[0] * m for _ in range(k)]
    for j, btn in enumerate(machine.buttons):
        for idx in btn:
            if idx < 0 or idx >= k:
                raise ValueError("Button index out of range.")
            affects[idx][j] = 1
    prob = pulp.LpProblem("joltage", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{j}", lowBound=0, cat=pulp.LpInteger) for j in range(m)]
    prob += pulp.lpSum(x)
    for i in range(k):
        prob += pulp.lpSum(affects[i][j] * x[j] for j in range(m)) == b[i]
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[status] != "Optimal":
        raise RuntimeError("No optimal solution.")
    return int(pulp.value(prob.objective))
def main() -> None:
    machines = parse_input("input.in")
    part1 = sum(min_presses_part1(mac) for mac in machines)
    part2 = sum(min_presses_part2(mac) for mac in machines)
    print("Part 1 solution:", part1)
    print("Part 2 solution:", part2)
if __name__ == "__main__":
    main()
