import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# 初始化 Pygame
pygame.init()

# 定义屏幕大小和颜色
SCREEN_SIZE = 600
CELL_SIZE = SCREEN_SIZE // 3
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)

# 创建窗口
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("第一届井字棋")

# 创建棋盘
board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
turn = 0

# 绘制棋盘
def draw_board():
    screen.fill(BG_COLOR)
    # 绘制网格线
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE), 5)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (SCREEN_SIZE, i * CELL_SIZE), 5)
    # 绘制棋子
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":      
                draw_x(row, col)
            elif board[row][col] == "O":
                draw_o(row, col)

def draw_x(row, col):
    # 绘制 X
    x1, y1 = col * CELL_SIZE + 50, row * CELL_SIZE + 50
    x2, y2 = (col + 1) * CELL_SIZE - 50, (row + 1) * CELL_SIZE - 50
    pygame.draw.line(screen, X_COLOR, (x1, y1), (x2, y2), 10)
    pygame.draw.line(screen, X_COLOR, (x2, y1), (x1, y2), 10)

def draw_o(row, col):
    # 绘制 O
    center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, O_COLOR, center, CELL_SIZE // 3, 10)

# 检查胜利
def check_win(player):
    # 检查行、列、对角线
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# 检查平局
def check_draw():
    return all(board[row][col] != " " for row in range(3) for col in range(3))

# 弹出胜利/平局提示
def show_message(message):
    pygame.display.set_caption(message)
    pygame.time.wait(2000)
    sys.exit()

# 主游戏循环
def game_loop():
    global turn
    while True:
        draw_board()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE

                # 检查点击是否有效
                if board[row][col] == " ":
                    current_player = players[turn % 2]
                    board[row][col] = current_player

                    # 检查游戏状态
                    if check_win(current_player):
                        draw_board()
                        pygame.display.flip()
                        show_message(f"玩家 {current_player} 胜利！")
                    elif check_draw():
                        draw_board()
                        pygame.display.flip()
                        show_message("游戏平局！")

                    turn += 1

if __name__ == "__main__":
    game_loop()
