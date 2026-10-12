def merge_sorted_array (nums1 , m , nums2 , n ) :
    nums2 = nums2[0:n] 
    for i in range(m,len(nums1)):
        nums1.pop()
    nums1.extend(nums2)
    nums1.sort()
    return nums1

    




print(merge_sorted_array(nums1 = [1, 2, 3, 0, 0, 0] , m = 3 , nums2 = [2, 5, 6] , n = 3))


# [1, 2, 2, 3, 5, 6]