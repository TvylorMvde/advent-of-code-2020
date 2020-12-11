filename = "slope.txt"

with open(f"advent-of-code-2020/day-03/{filename}") as file:
  lines = [line.strip() for line in file.readlines()]


def count_trees(right, down):
  x, y = 0, 0
  count = 0
  while y < len(lines):
    if lines[y][x % len(lines[0])] == "#":
      count += 1
    x += right
    y += down
  return count


# Part 1
print(count_trees(3, 1))


# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = 1

for slope in slopes:
  trees *= count_trees(*slope)

print(trees)
