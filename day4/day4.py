import re

filename = "passwords.txt"

with open(f"advent-of-code-2020/day4/{filename}", 'r') as file:
    lines = [password.strip("\n") for password in file.readlines()]


def check_hgt(hgt: str):
    if hgt.endswith("cm"):
        if 150 <= int(hgt[0: hgt.index("cm")]) <= 193:
            return True
    if hgt.endswith("in"):
        if 59 <= int(hgt[0: hgt.index("in")]) <= 76:
            return True
    return False


def validate_fields(password: dict):
    validations = []
    if len(password.keys()) == 7:
        for key, value in password.items():
            if key == 'byr':
                validations.append(1920 <= int(value) <= 2002)
            if key == 'iyr':
                validations.append(2010 <= int(value) <= 2020)
            if key == 'eyr':
                validations.append(2020 <= int(value) <= 2030)
            if key == 'hgt':
                validations.append(check_hgt(value))
            if key == 'hcl':
                validations.append(bool(re.match(r"^#[0-9a-fA-F]{6}$", value)))
            if key == 'ecl':
                ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                validations.append(value in ecls)
            if key == 'pid':
                validations.append(len(value) == 9)
        return all(validations)
    return False


passwords = []
start = 0
valid = 0

for i, line in enumerate(lines):
    if line == "":
        passwords.append(" ".join(lines[start:i]))
        start = i + 1

for password in passwords:
    password = {p.split(":")[0]: p.split(":")[1] for p in password.split() if 'cid' not in p}
    if validate_fields(password):
        valid += 1

print(valid)