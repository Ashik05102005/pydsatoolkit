class Node :
    def __init__(self , data) :
        self.data = data
        self.next = None 

class Stack :
    def __init__(self) :
        self.top = None

    def push(self , data) :
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None :
            return "stack is empty"
        val = self.top.data
        self.top = self.top.next
        return val
    
    def peek(self) :
        if self.top is None :
            return "stack is empty"
        return self.top.data

    def display(self) :
        current = self.top 
        while current :
            print(current.data , end=f"{" -> " if current.next else ""}")
            current = current.next
        print("")
        

stack = Stack()
for num in 10,20,30,40,50 :
    stack.push(num)
stack.display()

print(stack.pop())
print(stack.pop())

stack.display()

print(stack.peek())
