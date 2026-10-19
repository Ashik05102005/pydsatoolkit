class Node :
    def __init__(self , data) :
        self.data = data 
        self.next = None 


nums = [1,2,3,4,5,6,7,8]
head = None 
tail = None 

for num in nums :
    new_node = Node(num)
    if head is None :
        head = new_node
        tail = new_node
    else :
        tail.next = new_node
        tail = new_node

current = head
squares = []

while current :
    if current.next is None:
        print(current.data )
    else :
        print(current.data , end="->")
    squares.append(current.data ** 2)
    current = current.next
print("")
print(squares)


