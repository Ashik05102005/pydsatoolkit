from collections import deque

nums = 10,20,30,40
# stack
stack = deque()

#push
for num in nums :
    stack.append(num)

print(stack)

# pop
val = stack.pop()

print("removed data : ",val)
print(stack)

# peek
print("last element : ",stack[-1])


