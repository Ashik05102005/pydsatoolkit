
def insert_data(items , new_val , pos ) :
    items.append(None)
    for i in range(len(items) - 1 , pos , -1):
        items[i] = items[i - 1]
    items[pos] = new_val
    return items

def delete_data(items , index) : 
    for i in range(index , len(items)-1):
        items[i] = items[i+1]
    items.pop()
    return items
    

numbers = [1,2,3,4,5]
print(insert_data(numbers , 10 , 3))
print(delete_data(numbers , 2))
