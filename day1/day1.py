def get_list_of_numbers(filename):
    with open(f"advent-of-code-2020/day1/{filename}") as file:
        numbers = [int(number.strip()) for number in file.readlines()]
        return numbers


def part1(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j
    return None


def part2(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i * j * k
    return None


if __name__ == "__main__":
    numbers = get_list_of_numbers("numbers.txt")
    # Part 1
    print(part1(numbers))
    # Part 2
    print(part2(numbers))
