def solver(instructions):
    accumulator = 0
    visited = []
    i = 1
    
    while i < len(instructions):
        if i + 1 in visited:
            break
        
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
        
    return accumulator


def main(filename):
    with open(f"advent-of-code-2020/day-08/{filename}") as file:
        instructions = [line.strip() for line in file.readlines()]
    print(solver(instructions))


if __name__ == "__main__":
    main("instructions.txt")

    




