from collections import deque

nums = 10,20,30,40

queue = deque()

#enque 

for num in nums :
    queue.append(num) 

print(queue)

# deque 

val = queue.popleft()

print(val)

print(queue)

val = queue.popleft()

print(val)

print(queue)

