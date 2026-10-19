def insert_manually(items ,data , pos) :
    items.append(None )
    for i in range( len(items) - 1 , pos , -1) :
        items[i] = items[i - 1]
    
    items[pos] = data
    print("inserted , current list :",items)

    
def delete_manually(items , pos) :
    for i in (pos , len(items) - 2):
        # print(i)
        items[i] = items[i + 1] 
    items.pop()
    print("deleted , current list :" ,items)

def search_manually(items , target ) :
    for index in range(len(items)) :
        if items[index] == target :
            print("target found at index :" , index)

def reverse_manually(items ) :
    left = 0 
    right = len(items) - 1 
    while left <= right :
        items[left] , items[right] = items[right] , items[left] 
        left += 1
        right -= 1

    print("reversed :",items)

insert_manually([1,2,3,4,5,6,7] , 200 , 3)
delete_manually([1,2,3,4,5,6,7] , 5)
search_manually([1,2,3,4,5,6,7] , 5)
reverse_manually([1,2,3,4,5,6,7] )