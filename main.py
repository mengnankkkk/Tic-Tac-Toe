# 井字棋游戏

# 第一阶段：创建空棋盘并打印
def create_empty_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("---------")
    for row in board:
        print("|", " | ".join(row), "|")
    print("---------")

# 第二阶段：玩家输入并更新棋盘
def player_input(board, player):
    while True:
        try:
            move = int(input(f"玩家 {player}，请输入1到9之间的数字："))
            if move < 1 or move > 9:
                print("请输入1到9之间的数字！")
                continue

            # 将1-9的数字转换为棋盘位置的行列索引
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] != " ":
                print("这个位置已经被占用！")
                continue

            board[row][col] = player
            break
        except ValueError:
            print("请输入有效的数字！")

# 第三阶段：分析棋盘局势
def check_win(board, player):
    # 检查行、列和对角线是否有相同的符号
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    # 检查是否平局，棋盘没有空位并且没有赢家
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

# 第四阶段：开启双人对决
def game():
    board = create_empty_board()
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        current_player = players[turn % 2]
        player_input(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"玩家 {current_player} 胜利！")
            break

        if check_draw(board):
            print_board(board)
            print("游戏结束，平局！")
            break

        turn += 1

# 游戏入口
if __name__ == "__main__":
    game()
