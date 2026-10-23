class CircularQueue :
    def __init__(self , size):
        self.queue = [None] * size 
        self.size = size 
        self.count = 0
        self.front = 0 
        self.rear = 0

    def enqueue(self ,data) :
        if self.count == self.size :
            print("queue is full")
            return
        self.queue[self.rear] = data 
        self.rear = (self.rear + 1) % self.size 
        self.count += 1 
    
    def deque(self) :
        if self.count == 0 :
            # print("queue is empty")
            return "queue is empty"
        val = self.queue[self.front]
        self.queue[self.front] = None 
        self.front = (self.front + 1) % self.size 
        self.count -= 1
        return val

    def peek(self) :
        if self.count == 0 :
            # print("queue is empty")
            return "queue is empty"
        return self.queue[self.front]

queue = CircularQueue(5) 

for num in 10,20,30,40,50 :
    queue.enqueue(num) 

print(queue.queue)

print(queue.deque())
print(queue.deque())

print(queue.queue)

queue.enqueue(60)
# queue.enqueue(70)
queue.enqueue(70)
print(queue.queue)









