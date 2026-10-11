def two_sum (nums , target) :
    for index , num in enumerate(nums):
        for j in range(index + 1 ,len(nums)) :
            if num + nums[j] == target :
                return [index , j]

    return -1
print(two_sum(nums = [2, 7, 11, 15] , target = 9))
print(two_sum(nums = [3, 2, 4] , target = 6))
print(two_sum(nums = [3, 3] , target = 6))


