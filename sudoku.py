from sudoku_generator import SudokuGenerator
import sudoku_generator

game = 0
start = 0


def update_visuals():
    """
    :return: visual sudoku board (string) that contains sudoku                 puzzle numbers
    """
    global game
    all_digits = []
    for i in range(9):
        all_digits.extend(game.board[i])
    for index, num in enumerate(all_digits):
        if num == 0:
            all_digits[index] = ' '

    board_visual = ''
    space_row = ''
    i = 0
    while i < len(all_digits):
        if i != 0:
            if i % 3 == 0:
                board_visual += '  '
            if i % 9 == 0:
                board_visual += '\n'
            if i % 27 == 0:
                board_visual += f'\n{space_row}'
        board_visual += f'[{all_digits[i]}]'
        i += 1
    return board_visual


def solution_visual():
    global game
    all_digits = []
    for i in range(9):
        all_digits.extend(game.solution[i])
    for index, num in enumerate(all_digits):
        if num == 0:
            all_digits[index] = ' '

    board_visual = ''
    space_row = ''
    i = 0
    while i < len(all_digits):
        if i != 0:
            if i % 3 == 0:
                board_visual += '  '
            if i % 9 == 0:
                board_visual += '\n'
            if i % 27 == 0:
                board_visual += f'\n{space_row}'
        board_visual += f'[{all_digits[i]}]'
        i += 1
    return board_visual


def original_visual():
    global game
    all_digits = []
    for i in range(9):
        all_digits.extend(game.original[i])
    for index, num in enumerate(all_digits):
        if num == 0:
            all_digits[index] = ' '

    board_visual = ''
    space_row = ''
    i = 0
    while i < len(all_digits):
        if i != 0:
            if i % 3 == 0:
                board_visual += '  '
            if i % 9 == 0:
                board_visual += '\n'
            if i % 27 == 0:
                board_visual += f'\n{space_row}'
        board_visual += f'[{all_digits[i]}]'
        i += 1
    return board_visual


def check_results():
    win = False
    # print(game.board)
    # print(game.solution)
    if game.board == game.solution:
        win = True
    return win


def game_start():
    # Start screen
    global game
    global start
    print('Game modes:')
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    print('Select a option:', end=' ')
    option = int(input())
    if option == 1:
        game = SudokuGenerator(30, 9)
        game.fill_values()
        start = game.board
        endboard = start
        game.remove_cells()
        print(update_visuals())
    elif option == 2:
        game = SudokuGenerator(40, 9)
        game.fill_values()
        start = game.board
        game.remove_cells()
        print(update_visuals())
    elif option == 3:
        game = SudokuGenerator(50, 9)
        game.fill_values()
        start = game.board
        game.remove_cells()
        print(update_visuals())

    return game.board


def select_cell():
    print('What number would you like to insert?')
    number = input()
    if number == "0":
        print("Pick another number")
        select_cell()
    print('In which box?')
    box_num = input()
    print('In which cell?')
    cell_num = input()
    if box_num == "1":
        box = game.get_box(0, 0)
    elif box_num == "2":
        box = game.get_box(0, 4)
    elif box_num == "3":
        box = game.get_box(0, 7)
    elif box_num == "4":
        box = game.get_box(4, 0)
    elif box_num == "5":
        box = game.get_box(4, 4)
    elif box_num == "6":
        box = game.get_box(4, 7)
    elif box_num == "7":
        box = game.get_box(7, 0)
    elif box_num == "8":
        box = game.get_box(7, 4)
    elif box_num == "9":
        box = game.get_box(7, 7)
    x_val = 0
    y_val = 0
    if cell_num == "1":
        coordinates = box[0]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "2":
        coordinates = box[1]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "3":
        coordinates = box[2]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "4":
        coordinates = box[3]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "5":
        coordinates = box[4]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "6":
        coordinates = box[5]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "7":
        coordinates = box[6]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "8":
        coordinates = box[7]
        x_val = coordinates[1]
        y_val = coordinates[4]
        coordinates = [x_val, y_val]
    elif cell_num == "9":
        coordinates = box[8]
        x_val = coordinates[1]
        y_val = coordinates[4]
    coordinates = [x_val, y_val]
    if game.board[int(x_val)][int(y_val)] == 0:
        game.board[int(x_val)][int(y_val)] = int(number)
    else:
        print('This cell is full.')
        select_cell()


def game_won():
    # Game won screen
    print('Game won!')
    print('Press 0 to exit')


def game_lost():
    # Game lost screen
    print('Game over!')
    print('Press 1 to restart')


def main():
    global game
    print(update_visuals())


def won_game(board):
    won = False
    print(board)
    print(start)
    if board == start:
        won = True

    return won


if __name__ == "__main__":
    print('Welcome to Sudoku')
    # print(update_visuals())
game_start()
running = True
print("Input 0 after entering a value to end playing:")
select_cell()
print(update_visuals())
print('To exit press 0.')
print('To continue playing press 1.')
print('To reset the board, press 2')
print("To reset the game, press 3")
choice = input()
while running == True:
    if choice == "0":
        if not check_results():
            print("You lose")
        else:
            print("You win")
        print("Winning Board")
        print(solution_visual())
        print("Have a nice day")
        running = False
    elif choice == "1":
        select_cell()
        print(update_visuals())
        print('To exit press 0.')
        print('To continue playing press 1.')
        print('To reset the board, press 2')
        print("To reset the game, press 3")
        choice = input()
    elif choice == "2":
        game.board = game.original
        print(original_visual())
        print('To exit press 0.')
        print('To continue playing press 1.')
        print('To reset the board, press 2')
        print("To reset the game, press 3")
        choice = input()
    elif choice == "3":
        game_start()
        print('To exit press 0.')
        print('To continue playing press 1.')
        print('To reset the board, press 2')
        print("To reset the game, press 3")
        choice = input()

    else:
        print('To exit press 0.')
        print('To continue playing press 1.')
        print('To reset the board, press 2')
        print("To reset the game, press 3")
        choice = input()
