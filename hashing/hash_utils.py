# Question 1: Count Character Frequency
# Write a Python program to count the frequency of each character in a given string using a dictionary.
# Input:
# programming


data = "programming"

freq = {}

for char in data :
    freq[char] = freq.get(char , 0 ) +1
print(freq)

# Question 2: Find the First Non-Repeating Element
# Write a Python program to find the first non-repeating element in a list using a dictionary.
# Input:
# [4, 5, 1, 2, 1, 4, 5]

nums = [4, 5, 1, 2, 1, 4, 5]

num_dict = {}

for num in nums :
    num_dict[num] = num_dict.get(num , 0) + 1

for num , freq in num_dict.items() :
    if freq == 1 :
        print(num)
        break

# Question 3: Find Common Elements Between Two Lists
# Write a Python program to find the common elements between two lists using set intersection.
# Input:
# list1 = [1, 2, 3, 4, 5]list2 = [3, 4, 5, 6, 7]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = set(list1) & set(list2)


print(common)
