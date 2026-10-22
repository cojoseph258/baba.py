"""Morpion pour deux joueurs : lancer ce fichier dans le terminal."""

board = []


def display_board():
    print("    1   2   3")
    for index, row in enumerate(board, 1):
        print(f"{index}   " + " | ".join(row))
        if index < 3:
            print("   ---+---+---")


def player_input(player):
    while True:
        try:
            row = int(input(f"Joueur {player}, ligne (1-3) : ")) - 1
            column = int(input("Colonne (1-3) : ")) - 1
        except ValueError:
            print("Entre des nombres entiers.")
            continue
        if not (0 <= row < 3 and 0 <= column < 3):
            print("La ligne et la colonne doivent être entre 1 et 3.")
        elif board[row][column] != " ":
            print("Cette case est déjà occupée.")
        else:
            return row, column


def check_win(board, player):
    for index in range(3):
        if all(board[index][column] == player for column in range(3)):
            return True
        if all(board[row][index] == player for row in range(3)):
            return True
    return (all(board[i][i] == player for i in range(3))
            or all(board[i][2 - i] == player for i in range(3)))


def check_tie(board):
    return (all(cell != " " for row in board for cell in row)
            and not check_win(board, "X") and not check_win(board, "O"))


def play():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        display_board()
        row, column = player_input(player)
        board[row][column] = player
        if check_win(board, player):
            display_board()
            print(f"Le joueur {player} a gagné !")
            return player
        if check_tie(board):
            display_board()
            print("Match nul !")
            return "tie"
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    play()
