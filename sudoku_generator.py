import random


class SudokuGenerator:
    def __init__(self, removed_cells, row_length=9):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = 3
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.solution = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


    def get_board(self):
        """
        :return: 2D list of numbers that represents the board
        """
        return self.board

    def get_box(self, start_row, start_col):
        """
        :param start_row: row number of first row in box
        :param start_col: column number of first column in box
        :return: box number
        """
        if start_row <= 2 and start_col <= 2:
            box = ['[0][0]', '[0][1]', '[0][2]',
                   '[1][0]', '[1][1]', '[1][2]',
                   '[2][0]', '[2][1]', '[2][2]']
        elif start_row <= 2 and start_col <= 5:
            box = ['[0][3]', '[0][4]', '[0][5]',
                   '[1][3]', '[1][4]', '[1][5]',
                   '[2][3]', '[2][4]', '[2][5]']
        elif start_row <= 2 and start_col <= 8:
            box = ['[0][6]', '[0][7]', '[0][8]',
                   '[1][6]', '[1][7]', '[1][8]',
                   '[2][6]', '[2][7]', '[2][8]']
        elif start_row <= 5 and start_col <= 2:
            box = ['[3][0]', '[3][1]', '[3][2]',
                   '[4][0]', '[4][1]', '[4][2]',
                   '[5][0]', '[5][1]', '[5][2]']
        elif start_row <= 5 and start_col <= 5:
            box = ['[3][3]', '[3][4]', '[3][5]',
                   '[4][3]', '[4][4]', '[4][5]',
                   '[5][3]', '[5][4]', '[5][5]']
        elif start_row <= 5 and start_col <= 8:
            box = ['[3][6]', '[3][7]', '[3][8]',
                   '[4][6]', '[4][7]', '[4][8]',
                   '[5][6]', '[5][7]', '[5][8]']
        elif start_row <= 8 and start_col <= 2:
            box = ['[6][0]', '[6][1]', '[6][2]',
                   '[7][0]', '[7][1]', '[7][2]',
                   '[8][0]', '[8][1]', '[8][2]']
        elif start_row <= 8 and start_col <= 5:
            box = ['[6][3]', '[6][4]', '[6][5]',
                   '[7][3]', '[7][4]', '[7][5]',
                   '[8][3]', '[8][4]', '[8][5]']
        else:
            box = ['[6][6]', '[6][7]', '[6][8]',
                   '[7][6]', '[7][7]', '[7][8]',
                   '[8][6]', '[8][7]', '[8][8]']
        return box

    def print_board(self):
        """
        :return: void, displays the board to the console
        """
        print(self.board)

    def valid_in_row(self, row, num):
        """
        :param row: the index of the row we are checking
        :param num: the value we are looking for in the column
        :return: boolean
        """
        valid = True
        for i in range(len(self.board[row])):
            if self.board[row][i] == num:
                valid = False
                break
        return valid

    def valid_in_col(self, col, num):
        """
        :param col: the index of the column we are checking
        :param num: the value we are looking for in the column
        :return: boolean
        """
        valid = True
        for j in range(len(self.board)):
            for x in range(len(self.board[j])):
                if self.board[j][col] == num:
                    valid = False
                    break
            else:
                continue
            break
        return valid

    def valid_in_box(self, row_start, col_start, num):
        """
        :param row_start, col_start: the starting indices of the                                       box to check
        :param num: the value we are looking for in the box
        :return: boolean
        """
        valid = True
        x_vals = []
        y_vals = []
        i = 0
        box = self.get_box(row_start, col_start)
        while i < len(box):
            x_vals.append(int(box[i][1]))
            y_vals.append(int(box[i][4]))
            i += 1
        for j in range(len(x_vals)):
            for z in range(len(y_vals)):
                if self.board[x_vals[j]][y_vals[z]] == num:
                    valid = False
                    break
            else:
                continue
            break
        return valid

    def is_valid(self, row, col, num):
        """
        :param row, col: are the row index and col index of                                the cell to check in the board
        :param num: the value to test if it is safe to enter in                       this cell
        :return: boolean, if num's location satisfies game rules
        """
        valid = 0
        if self.valid_in_row(row, num):
            valid += 1
        if self.valid_in_col(col, num):
            valid += 1
        if self.valid_in_box(row, col, num):
            valid += 1
        if valid == 3:
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        """
        :param row_start: number of first row in box
        :param col_start: number of first column in box
        :return: void, fills 3x3 with randomly filled values
        """
        box = self.get_box(row_start, col_start)
        x_vals = []
        y_vals = []
        i = 0
        while i < len(box):
            x_vals.append(int(box[i][1]))
            y_vals.append(int(box[i][4]))
            i += 1
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        j = 0
        while j < 9:
            random_num = random.choice(numbers)
            self.board[x_vals[j]][y_vals[j]] = random_num
            self.solution[x_vals[j]][y_vals[j]] = random_num
            numbers.remove(random_num)
            j += 1

    def fill_diagonal(self):
        """
        :return: void, fills the three boxes of the board's main                   diagonal
        """
        self.fill_box(0, 0)
        self.fill_box(4, 4)
        self.fill_box(7, 7)

    def fill_remaining(self, row, col):
        """
        Second step in forming puzzle creates puzzle solution
        :param row, col: specify the coordinates of the first                              empty (0) cell
        :return: boolean, whether or not board was solved
        """
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                self.solution[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
                self.solution[row][col] = 0
        return False

    def fill_values(self):
        """
        :return: void, constructs a solution
        """
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        """
        :return: void, removes the appropriate number of cells                     from the board
        """
        zero_to_eighty = []
        for i in range(81):
            zero_to_eighty.append(i)

        def locate_cell(number):
            if 0 <= number <= 8:
                row = 0
            elif 9 <= number <= 17:
                row = 1
            elif 18 <= number <= 26:
                row = 2
            elif 27 <= number <= 35:
                row = 3
            elif 36 <= number <= 44:
                row = 4
            elif 45 <= number <= 53:
                row = 5
            elif 54 <= number <= 62:
                row = 6
            elif 63 <= number <= 71:
                row = 7
            elif 72 <= number <= 80:
                row = 8
            return row

        for i in range(self.removed_cells):
            number = random.choice(zero_to_eighty)
            row_num = locate_cell(number)
            col_num = number % 9
            coordinates = self.get_box(row_num, col_num)
            self.board[row_num][col_num] = 0
            zero_to_eighty.remove(number)


def generate_sudoku(size, removed):
    """
    :param size: how many boxes make up each side of the board
    :param removed: the amount of cells that will be cleared
    :return: size-by-size Sudoku board
    """
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
