class CircularQueue :
    def __init__(self , size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self , data) :
        if self.count == self.size :
            print("Que is full")
            return 
        self.queue[self.rear] = data
        self.rear = (self.rear + 1)%self.size
        self.count += 1

    def dequeue(self ) :
        if self.count == 0  :
            print("Queue is empty")
            return 
        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return val
    def peek(self):
        if self.count == 0  :
            print("Queue is empty")
            return 
        


que = CircularQueue(4)
print(que.queue)

que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
print(que.queue)

print(que.dequeue())
print(que.queue)
que.enqueue(50)
print(que.queue)
