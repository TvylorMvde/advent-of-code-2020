def get_list_of_passwords(filename):
    with open(f"advent-of-code-2020/day2/{filename}") as file:
        passwords = [line.strip().replace(":", "").split() for line in file.readlines()]
        return passwords


def get_password_policies(p):
    min_value, max_value = int(p[0].split("-")[0]), int(p[0].split("-")[-1])
    letter = p[1]
    word = p[-1]
    return min_value, max_value, letter, word


def part1(passwords):
    count = 0
    for p in passwords:
        min_val, max_val, letter, word = get_password_policies(p)
        if min_val <= word.count(letter) <= max_val:
            count += 1
    return count


def part2(passwords):
    count = 0
    for p in passwords:
        min_val, max_val, letter, word = get_password_policies(p)
        letter = p[1]
        word = p[-1]
        if word[min_val - 1] == letter and word[max_val - 1] != letter:
            count += 1
        elif word[min_val - 1] != letter and word[max_val - 1] == letter:
            count += 1
    return count


if __name__ == "__main__":
    passwords = get_list_of_passwords("passwords.txt")
    # Part 1
    print(part1(passwords))
    # Part 2
    print(part2(passwords))
