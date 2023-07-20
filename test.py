
board = [[" " for _ in range(3)] for _ in range(3)]


# Функция для отображения поля
def display_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)


# Функция для проверки победы
def check_win():
    # Проверяем строки
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Проверяем столбцы
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


# Функция для хода игрока
def make_move(player):
    while True:
        row = int(input("Введите номер строки (от 1 до 3): ")) - 1
        col = int(input("Введите номер столбца (от 1 до 3): ")) - 1

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = player
            break
        else:
            print("Некорректный ход. Попробуйте снова.")


# Основной игровой цикл
def play_game():
    current_player = "X"

    while True:
        display_board()
        print(f"Ходит игрок {current_player}")
        make_move(current_player)

        if check_win():
            display_board()
            print(f"Игрок {current_player} победил!")
            break

        # Проверяем на ничью
        if all(all(cell != " " for cell in row) for row in board):
            display_board()
            print("Ничья!")
            break

        # Меняем игрока
        current_player = "O" if current_player == "X" else "X"


# Запускаем игру
play_game()

