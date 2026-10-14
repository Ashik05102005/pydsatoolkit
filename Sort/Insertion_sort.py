nums = [5,3,1,8,2]

for i in range(1,len(nums)) :
    key = nums[i]
    j = i -1 
    while j >= 0 and nums[j] > key :
        nums[j+1] = nums[j]
        j-=1
        print(nums)
    nums[j+1] = key
    print("-----res-------")
    print(nums)
    print('-------------------------')

print(nums)
