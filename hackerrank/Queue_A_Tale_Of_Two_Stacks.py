class MyQueue:

    def __init__(self):
        self.inp = []
        self.out = []

    def peek(self):
        if len(self.out) > 0:
            return self.out[-1]
        self.__fill()
        return self.out[-1]

    def pop(self):
        if len(self.out) > 0:
            return self.out.pop()
        self.__fill()
        return self.out.pop()
    
    def __fill(self):
        while len(self.inp) > 0:
            self.out.append(self.inp.pop())

    def put(self, value):
        self.inp.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
