class Node :
    def __init__(self , data , next = None , prev = None ):
        self.data = data 
        self.next = next
        self.prev = prev


def display_ll(head) :
    current = head 
    print("--- forward ---")
    while current :
        print(f"| {None if current.prev is None else  current.prev.data} | {current.data} | {None if current.next is None else current.next.data} |" ,end="->")
        if current.next is None :
            break
        current = current.next
    print("\n--- backward ----\n")
    while current :
        print(f"| {None if current.prev is None else  current.prev.data} | {current.data} | {None if current.next is None else current.next.data} |" , end="<-")
        current = current.prev

    

def delete_from_begin(head) :
    if head is None or head.next is None :
        return None 
    new_head = head.next
    new_head.prev = None 
    return new_head

def delete_from_end(head) :
    if head is None or head.next is None :
        return None 

    current = head 
    while current.next :
        current = current.next

    prev_node = current.prev 
    prev_node.next = None 

    return head

def delete_specific_pos(head , pos ) :
    if head is None :
        return None 
    
    if pos == 0 :
        return delete_from_begin(head)
    
    current = head 
    for _ in range(pos - 1 ) :
        if current is None :
            print("Exceeded")
            return 
        current = current.next

    if current.next.next is None :
        current.next is None
        return head 

    next_node = current.next.next 
    current.next = next_node
    return head

def insertion_begin(head , data):
    new_node = Node(data)
    new_node.next = head 
    if head is not None :
        head.prev = new_node
    return new_node

def insertion_end(head , data ):
    new_node = Node(data)
    if head is None :
        return new_node
    current = head 
    while current.next :
        current = current.next 

    new_node.prev = current
    current.next = new_node
    return head

def insertion_specific_pos (head , data , pos) :
    
    
    
    new_node = Node(data)
    if head is None :
        if pos == 0 :
            return new_node
        else :
            print("Out of bounds")
            return None 
    if pos == 0 :
        return insertion_begin(head  , data)

    
    current = head
    for _ in range(pos - 1) :
        if current is None :
            print("limit reaches")
            return 
        current = current.next

    if current.next is None :
        current.next = new_node 
        new_node.prev = current
        return head
    
    next_node = current.next
    current .next = new_node
    new_node.prev , new_node.next = current , next_node
    next_node.prev = new_node

    return head
    
    
        


    

    

nums = [10,20,30,40,50,60]

head = None 
tail = None 

for num in nums :
    new_node = Node(data = num)
    if head is None :
        head = new_node
        tail = new_node
    else :
        # next_node = new_node
        tail.next  = new_node
        new_node.prev = tail
        tail = new_node

display_ll(head=head)

# head = delete_from_begin(head)

# display_ll(head=head)

# head = delete_specific_pos(head , 3)

# print("")
# display_ll(head=head)

head = insertion_begin(head , 1000)

display_ll(head)
