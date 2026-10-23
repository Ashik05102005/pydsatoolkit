# sorted
# -----------

nums =  [5,1,3,8,2]

# ---------- bubble Sort --------------- 


for i in range(len(nums)) :
    for j in range(len(nums) - i - 1 ) :
        if nums[j] > nums[j + 1] :
            nums[j] , nums[j + 1] = nums[j + 1] , nums[j]

print(nums)

# ------------- Selection Sort ---------------- 

for i in range(len(nums)) :
    min_index = i 
    for j in range(i , len(nums)) :
        if nums[min_index] > nums[j] :
            min_index = j
    nums[i] , nums[min_index] = nums[min_index] , nums[i]
print(nums)

# ------------- insertion sort ---------------- 

for i in range(1 , len(nums)) :
    key = nums[i]
    j = i-1
    while j>=0 and nums[j] > key :
        nums[j+1] = nums[j]
        j -= 1 
    nums[j + 1] = key

print(nums)