# from collections import deque

# queue = deque()

# # enque
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# queue.append(50)
# queue.append(60)

# print(queue)

# # deque
# val = queue.popleft()
# print(val)
# val = queue.popleft()
# print(val)


# # peek 
# print(queue[0])
# print(queue)

class Node :
    def __init__(self , data):
        self.data = data 
        self.next = None 

class Queue :
    def __init__(self):
        self.front = None
        self.rear = None 

    def enqueue(self , data) :
        new_node = Node(data)
        if self.front is None :
            self.front = new_node 
            self.rear = new_node 
        else :
            self.rear.next = new_node
            self.rear = new_node

    def deque(self) :
        if self.front is None :
            print("Queue is empty")
            return
        val = self.front.data
        self.front = self.front.next
        if self.front is None :
            self.rear = None 
        return val

    def peek(self ):
        if self.front is None :
            print("Queue is empty")
            return 
        print(self.front.data)
    
que = Queue()
que.enqueue(10)
que.enqueue(20)

res =que.deque()
print(res)

res =que.deque()
print(res)

que.peek()