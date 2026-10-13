class Node :
    def __init__(self , data  , next = None):
        self.data = data
        self.next = next 

class Stack :
    def __init__(self):
        self.top = None

    def push(self, data) :
        new_node = Node(data)
        new_node.next = self.top 
        self.top = new_node

    def pop(self ) :
        if self.top is None :
            return "Stack is empty"
        value = self.top.data 
        self.top = self.top.next

        return value

    def peek (self):
        if self.top is None :
            return "Stack is Empty"
        return self.top.data




stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

current = stack.top

while current :
    if current.next :
        print(f"[ {current.data} ]" , end= " -> ")
    else :
        print(f"[ {current.data} ]")
    current = current.next



