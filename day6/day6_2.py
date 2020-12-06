filename = "answers.txt"

with open(f"advent-of-code-2020/day6/{filename}", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

answers = []

start = 0
for i, line in enumerate(lines):
    if line == "":
        answers.append([set(line) for line in lines[start:i]])
        start = i + 1
    if i == len(lines) - 1:
        answers.append([set(line) for line in lines[start:i]])

intersections = []

for answer in answers:
    intersected = set.intersection(*answer)
    intersections.append(len(intersected))

print(sum(intersections))