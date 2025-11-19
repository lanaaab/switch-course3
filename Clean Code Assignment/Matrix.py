class Matrix:
    def __init__(self, rows, cols):
        self.board = []
        self.rows = rows
        self.cols = cols

    def generate_matrix(self):
        num = 1
        if self.rows == 0 and self.cols == 0:
            return
        for i in range(self.rows):
            self.board.append([])
            for j in range(self.cols):
                self.board[i].append(num)
                num += 1

    def print(self):
        for row in self.board:
            print("\t".join(map(str, row)))
        print("-----------------")

    def find_coordinate(self, value):
        for r in range(self.rows):
            if value in self.board[r]:
                c = self.board[r].index(value)
                return {'x': r, 'y': c}
        return None

    def get(self, row_num, col_num):
        return self.board[row_num][col_num]

    def print_row(self, row_num):
        for c in self.board[row_num]:
            print(c)

    def alter(self, row_num, col_num, new_value):
        self.board[row_num][col_num] = new_value


