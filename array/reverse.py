def delete_list (items) :
    left = 0 
    right = len(items) - 1
    while left < right :
        items[left] , items[right] = items[right] , items[left]
        left += 1
        right -= 1
    print(items)

delete_list([10,20,30,40,50])