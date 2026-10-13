def display_ll (queue) :
    current = queue.front

    while current :
        if current.next :
            print("[",current.data ,"]", end=" -> ")
        else :
            print("[",current.data ,"]")
        current = current.next

class Node :
    def __init__(self , data):
        self.data = data 
        self.next = None

class Queue :
    def __init__(self ):
        self.front = None 
        self.rear = None 

    def enqueue (self , data) :
        new_node = Node(data) 

        if self.rear is None :
            self.rear = new_node
            self.front = new_node
            return 

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None :
            return "Queue is Empty"
        value = self.front.data 
        self.front = self.front.next
        if self.front is None :
            self.rear = None 
        return value

    def peek(self) :
        if self.front is None :
            return "Queue is Empty"
        return self.front.data

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.enqueue(60)
queue.enqueue(70)



display_ll(queue)

print(queue.dequeue())

display_ll(queue)

print(queue.dequeue())

display_ll(queue)

print(queue.peek())