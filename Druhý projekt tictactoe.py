'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie 
author = Marek Illáš
email: m.illas@post.cz
discord: Marek I 
'''

import textwrap
from random import shuffle

VICTORY_CONDITIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def show_welcome():
    string = "Welcome to Tic Tac Toe game!"
    print(len(string) * "+")
    print(string)
    print("")


def show_rules():
    # \ to avoid empty line
    rules = """\
    GAME RULES:
    Each player can place one mark (or stone) per turn on the 3x3 grid
    The WINNER is who succeeds in placing three of their marks in a
    * horizontal,
    * vertical or
    * diagonal row
    Board schema (like Numpad on your keyboard):
    ---------
    7 | 8 | 9
    ---------
    4 | 5 | 6
    ---------
    1 | 2 | 3
    ---------
    """

    print(textwrap.dedent(rules))
    print("Play!")


def show_board(board):
    print_board = f"""\
    ---------
    {board[6]} | {board[7]} | {board[8]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[0]} | {board[1]} | {board[2]}
    ---------"""
    print(textwrap.dedent(print_board))


def update_board(board, player, space):
    board[space] = player


def check_is_empty(board, space):
    return board[space] == " "


def user_input(player):
    print(f"Player {player} |", end=" ")
    while True:

        try:
            space = int(input("Choose space(number): "))

            if space in range(1, 10):
                return space - 1
            else:
                print("Choose space in valid range 1-9")
                continue
        except ValueError:
            print("Choose number")


def check_victory(board, player):
    for x, y, z in VICTORY_CONDITIONS:
        if player == board[x] == board[y] == board[z]:
            return True
    return False


def check_is_tie(board):
    return " " not in board


def game_loop():
    board = [" " for i in range(9)]

    player_order = ["X", "O"]
    game = True

    shuffle(player_order)

    show_welcome()
    show_rules()
    show_board(board)
    while game:

        for player in player_order:

            while True:
                player_space = user_input(player)
                if not check_is_empty(board, player_space):
                    print("Space is occupied. Choose another space")
                    continue
                break

            update_board(board, player, player_space)
            show_board(board)
            if check_victory(board, player):
                print(f"Player {player} win!")
                game = False
                break

            if check_is_tie(board):
                print("It is tie, nobody win!")
                game = False
                break


if __name__ == "__main__":
    game_loop()