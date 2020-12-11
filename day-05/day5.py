filename = "seats.txt"

with open(f"advent-of-code-2020/day-05/{filename}") as file:
    seats = [line.strip() for line in file.readlines()]


def get_seat_row(seat):
    rows = list(range(0, 128))
    for char in seat[:7]:
        if char == "F":
            rows = rows[: len(rows) // 2]
        if char == "B":
            rows = rows[len(rows) // 2:]
    return rows[0]


def get_seat_column(seat):
    columns = list(range(0, 8))
    for char in seat[7:]:
        if char == "L":
            columns = columns[: len(columns) // 2]
        if char == "R":
            columns = columns[len(columns) // 2:]
    return columns[0]


def get_seat_id(seat):
    row = get_seat_row(seat)
    column = get_seat_column(seat)
    return row * 8 + column


if __name__ == "__main__":
    seats_ids = [get_seat_id(seat) for seat in seats]

    # Part 1 
    print(f"The highest seat ID: {max(seats_ids)}")

    # Part 2
    print(set(range(1000)) - set(seats_ids))
