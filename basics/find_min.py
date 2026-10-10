numbers = [2,5,1,9,8,7]

def find_min(nums):
    smallest = nums[0]
    for num in nums :
        if smallest > num :
            smallest = num
    return smallest

def find_min_pythonic(nums) : 
    return min(nums)


print(find_min(numbers))
print(find_min_pythonic(numbers))