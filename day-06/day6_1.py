filename = "answers.txt"

with open(f"advent-of-code-2020/day-06/{filename}", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

answers = []

start = 0
for i, line in enumerate(lines):
    if line == "":
        answers.append(" ".join(lines[start:i]))
        start = i + 1
    if i == len(lines) - 1:
        answers.append(" ".join(lines[start:]))

questions = []

for answer in answers:
    yeses = {i for i in answer if i.isalpha()}
    questions.append(len(yeses))

print(sum(questions))
