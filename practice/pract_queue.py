class Node :
    def __init__(self , data) :
        self.data = data
        self.next = None 

class Queue :
    def __init__(self ) :
        self.rear = None 
        self.front = None
    
    def enque(self , data) :
        new_node = Node(data)
        if self.front is None :
            self.front = new_node 
            self.rear = new_node
            return 
        self.rear.next = new_node 
        self.rear = new_node

    def deque(self ) :
        if self.front is None :
            return" queue is empty"
        val = self.front.data
        self.front = self.front.next 
        if self.front is None :
            self.rear = None
        return val

    def peek():
        if self.front is None :
            return" queue is empty"
        return self.front.data

    def display(self) :
        current = self.front 
        while current :
            print(current.data , end=f"{" -> " if current.next else ""}")
            current = current.next
        print("")

    
queue = Queue()

for num in 10,20,30,40,50,60 :
    queue.enque(num)

queue.display()

print(queue.deque())
print(queue.deque())

queue.display()

queue.enque(90)
queue.display()


