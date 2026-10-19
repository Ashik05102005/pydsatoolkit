# stack = [1,2,3]

# #push

# stack.append(4)
# stack.append(5)
# stack.append(7)
# stack.append(6)

# print(stack)

# #pop
# val = stack.pop()
# print("popped value :" , val , "\nlist :" , stack)

# # peek 
# print(stack[-1])

class Node :
    def __init__(self , data) :
        self.data = data
        self.next = None 

class Stack :
    def __init__(self):
        self.top = None 

    def push(self , data) :
        new_node = Node(data)
        new_node.next = self.top 
        self.top = new_node

    def pop(self ) :
        if self.top is None :
            print("The stack is empty. . . !")
            return
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self) :
        if self.top is None :
            print("The stack is empty. . . !")
            return
        return self.top.data