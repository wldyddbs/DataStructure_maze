#maze_Cqueue

#원형큐 + 스택 정답 생성

#텍스트 기반 UI 라이브러리
import curses
import time


class CQueue:
    def __init__(self, MaxQ = 100):
        self.front = 0
        self.rear = 0
        self.MaxQ = MaxQ
        self.items = [None] * self.MaxQ
        
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.MaxQ == self.front

    def enqueue(self, item):
        if item in self.items and item is not None:
            return  #중복이면 enq하지 않음
        if not self.isFull():
            self.rear = (self.rear + 1) % self.MaxQ
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.MaxQ
            return self.items[self.front]

    #원형큐 전체가 아닌 필요한 부분만 출력
    def __str__(self): 
        result = []
        i = self.front
        while i != (self.rear + 1) % self.MaxQ:
            result.append(str(self.items[i]))
            i = (i + 1) % self.MaxQ
        return "[" + ", ".join(result) + "]"


#미로를 보기 편하게 수정
def printMaze(stdscr):
    stdscr.clear()
    for row in maze:
        visual_row = " ".join("■" if cell == "1" else "·" if cell == "0" else ' ' if cell == ' ' else "☆" if cell == "2" else cell for cell in row)
        stdscr.addstr(visual_row + "\n")
    stdscr.refresh()

#1은 벽, 공백은 이미 방문한 곳. 이 둘을 제외
def isValidPos(x, y):
    if x < 0 or x >= MAZE_SIZE or y < 0 or y >= MAZE_SIZE:
        return False
    if maze[x][y] in ('1', ' '): 
        return False
    else:
        return True

#0은 안 간 길, 공백은 간 길, 2는 간 벽
def wall(x, y):
    if x < 0 or x >= MAZE_SIZE or y < 0 or y >= MAZE_SIZE:
        return False
    if maze[x][y] in ('0',' ','e','x','2'):
        return False
    else:
        return True

m = [
    '1111111111111111111111111111111111111111111111111',
    'e000100000001000000000100000100000000000000000001',
    '1110111010101011111110101010101011111110111110111',
    '1010001010101000001010101010101010000000100010001',
    '1011101110101011101010111010101010111110101011111',
    '1010001000101010001010001010001010100010101000101',
    '1010111011101010111011101011111010101011101110101',
    '1010001010001010001000100010000010001000101010001',
    '1011101010111011101010111110111111111110101011101',
    '1000100010001010001010001000100000000010100000101',
    '1010111111101110111010111011111110111010111011111',
    '1010000000100000100010100010000010101010000010001',
    '1011111110111111101011101110111010101010111110101',
    '1010001000100000001000001000101000100010100000101',
    '1010101111101111111111111011101111101110101111101',
    '1000100000001000000000100010000000101000101000001',
    '1011111111111011101110111010111010101110101011101',
    '1010000000000010100010000010101010100010101000101',
    '1011111011111110111011111110101011111010101110111',
    '1010001000100000100010000010001010000010100010001',
    '1010101110101011101110101111101010111110111011111',
    '1000100010001010001000100000001010001000101000001',
    '1111111010111110111111111111111010101011101111101',
    '1000100010100010100000000010000010100000000000101',
    '1010101110101010101011111010111010111011111111101',
    '1010001000101010101000100000100010001010000000001',
    '1011111011101010111010111111101111101010111111101',
    '1010000010001010001010001000000010001010101000101',
    '1011111110111010101111101011111110111110101010101',
    '1000000010001010100010001010001000100010101010001',
    '1111111011101010111010111110101011101010101011111',
    '1010001000101010001010000010100010001000100010001',
    '1010101110101011111010111010111111101111101111101',
    '1010100010001000100010001010100000001000101000001',
    '1010111011111110101111111010101011111010101011101',
    '1010100000000010001000000010101000000010100010001',
    '1010101110111111111011101110111111111110111110111',
    '1000100010100000001000101000100010000000100010001',
    '1111111011101110111010111011101010111111101111101',
    '1000000000101010100010000010001000100000100000111',
    '1110111010101010101111111110111011111011101010001',
    '1000001010101010100010001000001010001000001000111',
    '1011111010101010111010101011101110101110111110101',
    '1000001010100010001000101000100000100010000010001',
    '1111101010111011101111101111111110111011111011111',
    '1000001010100010100010001000100010001010000010001',
    '1011111010101110111010111010101011111010111111101',
    '1010000010000000001000000010001000000000000000001',
    '1x11111111111111111111111111111111111111111111111'
]
    

maze = [list(row) for row in m]
MAZE_SIZE = 49
    

def BFS(stdscr):
    s = CQueue()
    s.enqueue((1, 0, None)) #출발점 좌표
    while not s.isEmpty():
        here = s.dequeue()
        x, y,_= here
        ex = here[2]


        #도착 지점에 도달했을 때
        if maze[x][y] == 'x':
            printMaze(stdscr) #최종 지도 유지
            stdscr.addstr("도착!", curses.A_BOLD)
            print(s)
            stdscr.refresh()
            stdscr.getch()  # 사용자 입력 대기
            return True

        #방문 표시
        maze[x][y] = ' '  
        printMaze(stdscr) #미로 출력
        print(s) #스택 출력
        time.sleep(0.01)

        #이동 가능한 방향 확인 후 스택에 푸시
        if isValidPos(x, y-1): s.enqueue((x, y-1,(x, y)))
        if isValidPos(x, y+1): s.enqueue((x, y+1,(x, y)))
        if isValidPos(x-1, y): s.enqueue((x-1, y,(x, y)))
        if isValidPos(x+1, y): s.enqueue((x+1, y,(x, y)))

    
    printMaze(stdscr)
    stdscr.addstr("길을 찾을 수 없음")
    stdscr.refresh()
    stdscr.getch() #사용자 입력 대기 
    return False

#벽 분류
def changeWall(stdscr):
    d = CQueue()
    wallstart=((0,0))
    d.enqueue(wallstart)
    x, y = wallstart

    #큐가 비어야 종료
    while not d.isEmpty():
        wallstart = d.dequeue()
        x, y = wallstart

        #방문 표시는 2
        maze[x][y] = '2'  
        printMaze(stdscr)  # 미로 출력
        print(d) #스택 출력
        time.sleep(0.01)

        #이동 가능한 방향 확인 후 스택에 푸시
        if wall(x, y-1): d.enqueue((x, y-1))
        if wall(x, y+1): d.enqueue((x, y+1))
        if wall(x-1, y): d.enqueue((x-1, y))
        if wall(x+1, y): d.enqueue((x+1, y))

    printMaze(stdscr)
    stdscr.addstr(" ")
    stdscr.refresh()
    stdscr.getch() #사용자 입력 대기

curses.wrapper(BFS)
curses.wrapper(changeWall)