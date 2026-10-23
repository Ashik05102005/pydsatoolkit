nums = [10,20,30,40,50,60]
target = 10

for index , num in enumerate(nums) :
    if num == target :
        print(num , "at index :" , index)
        break 
        
left = 0
right = len(nums) - 1
while left <= right :
    mid = (left + right) // 2 
    if nums[mid] == target :
        print(nums[mid] ,"found at index :" , mid)
        break
    elif nums[mid] < target :
        left = mid + 1
    else :
        right = mid - 1 