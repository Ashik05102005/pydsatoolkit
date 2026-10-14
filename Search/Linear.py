nums = [10,20,30,40,50,60,70]
target = 50

for i in range(len(nums)):
    if nums[i] == target :
        print(f"{target} is found at index : {i}")
        break
    