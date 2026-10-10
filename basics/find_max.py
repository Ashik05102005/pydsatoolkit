def find_max (nums) : 
    largest = 0
    for num in nums : 
        if largest < num :
            largest = num 
    return largest

def find_max_Pythonic (nums):
    return max(nums)

print(find_max([2,5,1,9,8,7]))
print(find_max_Pythonic([2,5,1,9,8,7]))

