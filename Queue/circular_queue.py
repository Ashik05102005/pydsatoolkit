class CircularQueue :
    def __init__(self , size) :
        self.queue = [None] * 5
        self.size = size
        self.rear = 0
        self.front = 0
        self.count = 0

    def enqueue(self , data) :
        if self.count == self.size :
            print("Queue is Full  ")
            return
        self.queue[self.rear] = data
        self.rear = (self.rear + 1 ) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0 :
            print("Q is Empty")
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = ( self.front + 1 ) % self.size
        self.count -= 1
        return value

    def peek(self) :
        if self.count == 0 :
            print("Q is empty")
        return self.queue[self.front]
    
queue = CircularQueue(5)

queue.enqueue(1)
print(queue.rear)
queue.enqueue(2)
print(queue.rear)
queue.enqueue(3)
print(queue.rear)
queue.enqueue(4)
print(queue.rear)
queue.enqueue(5)
print(queue.rear)


print(queue.queue)


queue.dequeue()
print(queue.front)
queue.dequeue()
print(queue.front)
print(queue.queue)


print(queue.peek())