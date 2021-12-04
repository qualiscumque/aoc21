import sys

data = []
with open("../input/input.txt") as f:
  data = [line.strip() for line in f.readlines()]

boards = []
random_nums = data[0]
board_data = data[1:]


class BingoBoard:
    board_num = 0
    data = []
    markers = []

    def __init__(self, board_num):
        self.data = []
        self.markers = []
        self.board_num = board_num

    def add_line(self, line):
        nums = (" ".join(line.split())).split(" ")
        self.data.append([int(entry) for entry in nums])

    def add_number(self, num: int):
        for y, row in enumerate(self.data):
            for x, col in enumerate(self.data[y]):
                if self.data[y][x] == num:
                    self.markers.append((x, y),)

        if self.check_win():
            unmaked_sum = self.sum_unmarked()
            print(f"board {self.board_num} won with numer {num}")
            print(f"unmarked sum {unmaked_sum}")
            print(f"multiply by {num} == {unmaked_sum * num}")
            return 1

    def check_win(self):
        def check_line():
            for y in list(range(len(self.data))):
                line_complete = True
                for x in list(range(len(self.data[1]))):
                    if (x, y) not in self.markers:
                        line_complete = False
                if line_complete:
                    return True

        def check_col():
            for x in list(range(len(self.data))):
                col_complete = True
                for y in list(range(len(self.data[1]))):
                    if (x, y) not in self.markers:
                        col_complete = False
                if col_complete:
                    return True

        if check_line() or check_col():
            return True
        return False

    def sum_unmarked(self):
        sum = 0
        for y in list(range(len(self.data))):
            for x in list(range(len(self.data[1]))):
                if (x, y) not in self.markers:
                    sum += self.data[y][x]
        return sum


def parse_boards(data):
    board = None
    board_num = 0
    for line in data:
        if line == "":
            if board:
                boards.append(board)
                board_num += 1
            board = BingoBoard(board_num)
        else:
            board.add_line(line)
    if board:
        boards.append(board)

parse_boards(board_data)


for num in [int(num) for num in random_nums.split(",")]:
    for board in boards:
        if board.add_number(num) == 1:
            sys.exit()

print(boards)

