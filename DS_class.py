#스택과 큐의 클래스들입니다.

#스택

class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0
    
    def push(self, item):
        if item in self.top:
            return
        else:
             self.top.append(item) #full 0에서 건너뛰는 문제 질문
    
    def pop(self):
        if not self.isEmpty():
            return self.top.pop()
        
    #top과 item의 인덱스(미로의 몇번째 전진인지)를 비교해, 되돌아온 상황이라면 틀린 길을 모두 삭제하고 옳은 길을 추가하는 push입니다.
    def valid_push(self,item):
        while not self.isEmpty() and self.top[-1][2] >= item[2]:
            self.top.pop()
        self.push(item)
    
    def clear(self):
        self.top = []

    def __str__(self):
        return str(self.top)
    

#원형큐

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
        #i가 rear+1이 될 때까지 반복
        while i != (self.rear + 1) % self.MaxQ:
            result.append(str(self.items[i]))
            i = (i + 1) % self.MaxQ
        return "[" + ", ".join(result) + "]"