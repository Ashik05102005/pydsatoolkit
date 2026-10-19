class Node :
    def __init__(self , data):
        self.data = data
        self.next = None

class Ll :
    def __init__(self):
        self.top = None 

list1 = Ll()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

list1.top = node1
list1.top.next = node2    
list1.top.next.next = node3   
