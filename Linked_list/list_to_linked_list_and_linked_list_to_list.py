
print("------- List To Linked List -------")

class Node :
    def __init__(self , data):
        self.data = data 
        self.next = None

Numbers = [10,20,30,40,50,60]

head = None 
tail = None 

for num in Numbers :
    new_node = Node(num)

    if head is None :
        head = new_node 
        tail = new_node
    else :
        tail.next = new_node 
        tail = new_node

current = head 

while current :
    print(current.data) 
    current = current.next 

print("------- Linked List To List -------")

squares = []

current = head 

while current :
    squares.append(current.data ** 2)
    current = current.next

print(squares)
