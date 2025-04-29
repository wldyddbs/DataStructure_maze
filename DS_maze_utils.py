
#미로를 보기 편하게 수정
def printMaze(stdscr,maze):
    stdscr.clear()
    for row in maze:
        visual_row = " ".join("■" if cell == "1" else "·" if cell == "0" else ' ' if cell == ' ' else "☆" if cell == "2" else cell for cell in row)
        stdscr.addstr(visual_row + "\n")
    stdscr.refresh()


def isValidPos(x, y,maze, MAZE_SIZE):
    if x < 0 or x >= MAZE_SIZE or y < 0 or y >= MAZE_SIZE:
        return False
    if maze[x][y] in ('1', ' '):
        return False
    else:
        return True


def wall(x, y,maze, MAZE_SIZE):
    if x < 0 or x >= MAZE_SIZE or y < 0 or y >= MAZE_SIZE:
        return False
    if maze[x][y] in ('0', ' ','e','x','2','+'):
        return False
    else:
        return True