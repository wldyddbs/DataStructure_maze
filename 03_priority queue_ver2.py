#priority queue

#텍스트 기반 UI 라이브러리
import curses
import time
from DS_class import Stack

class PriorityQueue:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []

    def enqueue(self, item):
        if item in self.items and item is not None:
            return
        else:
            self.items.append(item)

    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1,self.size()):
                if self.items[i][3] > self.items[highest][3]:
                    highest = i
            return highest
    
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self. items.pop(highest)
        
    def __str__(self):
        return str(self.items)
    
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

# 거리 함수 정의
def dist(x, y):
    return abs(x-49) + abs(y - 1)

countnum = Stack()

def PrioritySearch(stdscr):
    q = PriorityQueue()
    num = 0
    q.enqueue((1,0,num,-dist(1,0)))
    countnum.push((1,0,num))
    print('PQueue: ')

    while not q.isEmpty():
        here =  q.dequeue()
        print(here)
        x,y,_,_=here
        countnum.check_push(here)
        if (maze[x][y]=='x'):
            printMaze(stdscr) #최종 지도 유지
            stdscr.addstr("도착!", curses.A_BOLD)
            print(q)
            stdscr.refresh()
            stdscr.getch() #사용자 입력 대기
            return True
        #방문 표시
        maze[x][y] = ' '
        printMaze(stdscr) #미로 출력

        num = countnum.top[-1][2] + 1

        if isValidPos(x, y-1): q.enqueue((x, y-1, num, -dist(x,y-1))) 
        if isValidPos(x, y+1): q.enqueue((x, y+1, num, -dist(x,y+1)))  
        if isValidPos(x-1, y): q.enqueue((x-1, y ,num, -dist(x-1,y)))
        if isValidPos(x+1, y): q.enqueue((x+1, y, num, -dist(x+1,y)))
        
        print(q)
        stdscr.getch() #사용자 입력 대기

    printMaze(stdscr)
    stdscr.addstr("길을 찾을 수 없음")
    stdscr.refresh()
    stdscr.getch() #사용자 입력 대기 
    return False

def correct_path(stdscr):
    for i in countnum.top:
        x,y,_,_= i
        maze[x][y]='+'
        printMaze(stdscr) #미로 출력
        time.sleep(0.01)
        print(i)
    printMaze(stdscr) #최종 지도 유지
    stdscr.refresh()
    stdscr.getch() #사용자 입력 대기
    return True

curses.wrapper(PrioritySearch)

curses.wrapper(correct_path)
