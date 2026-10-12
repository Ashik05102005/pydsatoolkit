def remove_duplicates(nums) :
    num_set = set(nums) 
    nums.clear()
    for num in num_set :
        nums.append(num)
    nums.sort()
    return nums

print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))



