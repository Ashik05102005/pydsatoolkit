class Node :
    def __init__(self , data) :
        self.data = data 
        self.next = None 
        self.prev = None 

class Doubly_ll :
    def __init__(self) :
        self.head = None 
        self.tail = None

    def add_node(self , data ) :

        new_node = Node(data) 

        if self.head is None  :
            self.head = new_node
            self.tail = new_node
            return 

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_from_begin(self ) :
        if self.head is None or self.head.next is None :
            self.head = None
            return 
        self.head = self.head.next
        self.head.prev = None 

    def remove_from_end(self) :
        if self.head is None or self.head.next is None :
            return None 

        current = self.head 
        while current.next.next :
            current = current.next

        current.next = None

    def remove_specific_pos(self , pos) :
        if self.head is None :
            return None 

        current = self.head 

        for _ in range(1 ,pos - 1) :
            if current.next is None :
                print("limit exceedss")
                return 
            current = current.next

        print(current.data)

        next_node = current.next.next

        current.next = next_node

        if next_node :
            next_node.prev = current 
    
    def insert_to_begin(self , data) :

        new_node = Node(data) 

        if self.head is None :
            self.head = new_node
            return

        self.head.prev = new_node 

        new_node.next = self.head 

        self.head = new_node

    def insert_to_end(self , data) :

        new_node = Node(data)

        if self.head is None :
            return new_node

        current = self.head 

        while current.next :
            current = current.next 

        new_node.prev = current 

        current.next = new_node

    def insert_specific_pos(self , data , pos) :

        new_node = Node(data) 

        if pos == 0 and self.head :
            new_node.next = self.head
            self.head.prev = new_node
            return 

        if self.head is None or self.head.next is None :
            return 

        current = self.head 

        for _ in range(1 , pos-1) :
            if current is None :
                print("range exceeded ")
                return 
            current = current.next

        print(current.data)

        next_node = current.next 
        new_node.next , new_node.prev = next_node , current
        next_node.prev = new_node
        current.next = new_node
        return 
            
        
    def display(self) :
        current = self.head 
        while current :
            if current.next :
                print(f"| {current.prev.data if current.prev else current.prev} | {current.data} | {current.next.data if current.next else current.next} |" , end = " <---> ")
            else :
                print(f"| {current.prev.data if current.prev else current.prev} | {current.data} | {current.next.data if current.next else current.next} |" )
                
            current = current.next
        print("")

d_ll = Doubly_ll()

d_ll.add_node(10)
d_ll.add_node(20)
d_ll.add_node(30)
d_ll.add_node(40)
d_ll.add_node(50)

d_ll.display()

d_ll.remove_from_begin()

d_ll.display()

d_ll.remove_specific_pos(2)

d_ll.display()

d_ll.remove_specific_pos(3)

d_ll.display()

d_ll.insert_to_begin(00)

d_ll.display()

d_ll.insert_to_begin(-10)

d_ll.display()

d_ll.insert_to_end(50)

d_ll.display()

d_ll.insert_specific_pos(5 , 5)

d_ll.display()
