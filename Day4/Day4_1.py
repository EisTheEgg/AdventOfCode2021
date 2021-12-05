# https://adventofcode.com/2021/day/4

input = open("input.txt")
lines = input.readlines()

commands = lines[0].split(",")
lines.pop(0)
lines.pop(0)

BOARD_SIZE = 5
final_score = None

drawn_numbers = {}

class Board:
    instances = []

    def __init__(self, index):
        start = index
        end = start + BOARD_SIZE

        board_lines = []

        for idx in range(start, end):
            row = lines[idx].split()
            board_lines.append(row)

        self.rows = board_lines
        self.__class__.instances.append(self)

    def get_sum_of_unmarked(self):
        unmarked_sum = 0

        for row in self.rows:
            for number in row:
                if number not in drawn_numbers:
                    unmarked_sum += int(number)

        return unmarked_sum

    def get_columns(self):
        columns = []

        for i in range(BOARD_SIZE):
            column = []

            for row in self.rows:
                column.append(row[i])

            columns.append(column)

        return columns

    def update(self):
        success = False

        for row in self.rows:
            row_success = True

            for number in row:
                if number not in drawn_numbers:
                    row_success = False
                    break

            if row_success:
                success = True
                break

        if success:
            return success

        for column in self.get_columns():
            column_success = True

            for number in column:
                if number not in drawn_numbers:
                    column_success = False
                    break

            if column_success:
                success = True
                break

        return success
    

for i in range(0, len(lines), BOARD_SIZE + 1):
    Board(i)

for command in commands:
    drawn_numbers[command] = True

    for board in Board.instances:
        result = board.update()

        if result:
            final_score = board.get_sum_of_unmarked() * int(command)
            break

    if final_score is not None:
        break

print(final_score)
