class Node :
    def __init__ (self , data) :
        self.data = data
        self.next = None


def insert_begining(head , data) :
    new_node = Node(data)

    new_node.next = head

    head = new_node

    return head

def insert_end(head , data) :

    new_node = Node(data)

    if head is None :
        return new_node

    current = head 

    while current.next is not None :
        current = current.next 

    current.next = new_node

    return head

def insert_specific_position(head , data , pos ) :

    new_node = Node(data)

    if pos == 0 :
        new_node.next = head
        display_linked_list(new_node)
        return new_node

    current = head 

    for _ in range(pos - 1):

        if current.next is None :
            raise IndexError("out of range")

        current = current.next 

    new_node.next = current.next 
    current.next = new_node

    display_linked_list(head)

    return head
        

def display_linked_list(head):

    current = head

    while current :
        if current.next is None :
            print(current.data)

        else :
            print(current.data , end=" -> ")

        current = current.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = insert_begining(head=head , data=00)
display_linked_list(head)
print("")
head = insert_end(head=head , data=40)
display_linked_list(head)
print("")

head = insert_begining(head , -10)
display_linked_list(head)
print("")

head = insert_specific_position(head , 77  , 6)
