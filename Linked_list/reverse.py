class Node :
    def __init__ ( self , data ) :
        self.data = data  
        self.next = None

def display_ll (head) :
    current = head 

    while current :
        if current.next :
            print("[",current.data ,"]", end=" -> ")
        else :
            print("[",current.data ,"]")
        current = current.next


def reverse_ll (head) :
    previous = None 
    current = head

    while current :
        new_node = current.next 
        current.next = previous

        previous = current
        current = new_node

    display_ll(previous)
    return previous

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

reverse_ll(head=head)




