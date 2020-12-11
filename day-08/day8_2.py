def solver(instructions):
    visited = []
    accumulator = 0
    i = 1

    while i < len(instructions):
        if i in visited:
            return False, accumulator
        
        visited.append(i)
        operation, value = instructions[i - 1].split()
        value = int(value)
        
        if operation == "nop":
            i += 1
        if operation == "acc":
            accumulator += value
            i += 1
        if operation == "jmp":
            i += value

    return True, accumulator


def part2(instructions):
    for i, operation in enumerate(instructions):
        tokens = operation.split()
        fixed = []
        if tokens[0] == "nop":
            fixed = instructions[:i] + ["jmp " + tokens[1]] + instructions[i+1:]
        elif tokens[0] == "jmp":
            fixed = instructions[:i] + ["nop " + tokens[1]] + instructions[i+1:]
        if fixed != []:
            solved = solver(fixed)
            if solved[0]:
                return solved[1]


def main(filename):
    with open(f"advent-of-code-2020/day-08/{filename}") as file:
        instructions = [line.strip() for line in file.readlines()]
    print(part2(instructions))


if __name__ == "__main__":
    main("instructions.txt")
