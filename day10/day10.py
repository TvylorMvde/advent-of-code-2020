def get_list_of_adapters(filename):
    with open(f"advent-of-code-2020/day10/{filename}") as file:
        adapters = [int(line.strip()) for line in file.readlines()]
        return adapters


def get_list_of_differences(adapters):
    differences = []
    adapters = sorted(adapters)
    adapters.insert(0, 0)
    for i in range(len(adapters) - 1):
        n1, n2 = adapters[i], adapters[i + 1]
        differences.append(n2 - n1)
    return differences


def get_all_adapters_arrangements(adapters):
    last = max(adapters)
    index = [1] + [0] * last
    print(index)
    for i in sorted(adapters):
        index[i] = index[i-1] + index[i-2] + index[i-3]
        if i == last:
            return index[i]


if __name__ == "__main__":
    adapters = get_list_of_adapters("adapters.txt")
    differences = get_list_of_differences(adapters)
    # Part 1
    print(differences.count(1) * (differences.count(3) + 1))
    # Part 2
    print(get_all_adapters_arrangements(adapters))




