class Node :
    def __init__(self , data) :
        self.data = data
        self.prev = None 
        self.next = None 

nums = [1,2,3,4,5,6]

head = None 
tail = None 

for num in nums :
    new_node = Node(num) 
    if head is None :
        head = new_node
        tail = new_node
    else  :
        new_node.prev = tail
        tail.next = new_node
        tail = new_node

current = head 
squares = []

while current :
    print(f"| {current.prev.data if current.prev else None} | {current.data} | {current.next.data if current.next else None} |" , end=f" {" -> " if current.next else ""} " ) 
    squares.append(current.data ** 2)
    current = current.next

print("")
print(squares)

