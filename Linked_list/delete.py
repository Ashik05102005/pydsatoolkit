class Node :
    def __init__(self , data):
        self.data = data 
        self.next = None

def display_ll (head) :
    current = head 
    while current :
        if current.next :
            print(current.data , end="->") 

        else :
            print(current.data)
        
        current = current.next 


def delete_from_begin (head) :

    if head is None or head.next is None :
        print(None)
        return None
    
    head = head.next

    display_ll(head) 

    return head   

def delete_from_end (head) :

    if head.next is None  or head is None :
        return None

    current = head 

    while current.next.next :
        current = current.next 

    current.next = None

    display_ll(head)

    return head

def delete_specific_pos (head , pos) :

    if pos == 0 :
        head = head.next
        return head

    current  = head 
    for _ in range(pos - 1 ):

        if current.next is None :
            return head 
        
        current = current.next

    if current.next is None :
        return head
        
    current.next = current.next.next

    display_ll(head)

    return head



    
    

head  = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("")

delete_from_end(head)
