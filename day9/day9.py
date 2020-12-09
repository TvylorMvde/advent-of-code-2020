def get_list_of_numbers(filename):
    with open(f"advent-of-code-2020/day9/{filename}") as file:
        numbers = [int(number.strip()) for number in file.readlines()]
        return numbers
    

def find_invalid_number(numbers):
    start = 0
    end = 25
    
    while start < len(numbers):
        preambles = numbers[start: end]
        target = numbers[end]
        if sum_checker(preambles, target):
            start += 1
            end += 1
            continue
        break
    return target


def sum_checker(preambles, target):
    for i in preambles:
        for j in preambles:
            if i + j == target:
                return True
    return False
    

def find_encryption_weakness(numbers, invalid_number):
    sublists = []
    for i in range(len(numbers) + 1):
        for j in range(i + 1, len(numbers) + 1):
            sublist = numbers[i:j]
            sublists.append(sublist)
    for sublist in sublists:
        if len(sublist) >= 2:
            if sum(sublist) == invalid_number:
                return min(sublist) + max(sublist)
    return None


if __name__ == "__main__":
    # Part 1
    numbers = get_list_of_numbers("numbers.txt")
    invalid_number = find_invalid_number(numbers)
    print(invalid_number)
    # Part 2
    enc_weakness = find_encryption_weakness(numbers, invalid_number)
    print(enc_weakness)

    
    
