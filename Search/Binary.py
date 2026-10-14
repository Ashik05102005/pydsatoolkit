nums = [10,20,30,40,50,60,70]
target = 50

low = 0 
high = len(nums) - 1

while low <= high :
    mid = (high + low) // 2
    if nums[mid] == target :
        print(f"{target} find at index : {mid}")
        break
    elif nums[mid] < target :
        low = mid + 1
    else :
        high = mid - 1
