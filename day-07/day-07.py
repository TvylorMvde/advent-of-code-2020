def get_data(filename):
    with open(f"day-07/{filename}") as file:
        data = [line.strip() for line in file.readlines()]
        return data


def get_number_of_bags(color):
    bags = []
    for d in data:
        if color in d and d.index(color) != 0:
            bags.append(d)

    all_colors = []

    if len(bags) == 0:
        return []
    else:
        colors = [bag[:bag.index(" bags")] for bag in bags]
        colors = [color for color in colors if color not in all_colors]

        for color in colors:
            all_colors.append(color)
            bags = get_number_of_bags(color)

            all_colors += bags

        uniqueColors = []
        for color in all_colors:
            if color not in uniqueColors:
                uniqueColors.append(color)
        
    return uniqueColors


def count_bags(color):
    rule = ""
    for d in data:
        if d[:d.index(" bags")] == color:
            rule = d

    if "no" in rule:
        return 1

    rule = rule[rule.index("contain") + 8:].split()

    total = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        color = rule[i + 1] + " " + rule[i + 2]
        total += count * count_bags(color)
        i += 4

    return total + 1

    
if __name__ == "__main__":
    data = get_data("bags.txt")
    # Part 1
    print(len(get_number_of_bags("shiny gold")))
    # Part 2
    print(count_bags("shiny gold"))
