numbers = [5, 3, 8, 1, 2 ,1,2,1,1,1,3]

for i in range(len(numbers)) :
    min_index = i 
    for j in range(i+1 , len(numbers)):
        if numbers[min_index] > numbers[j] :
            min_index = j
    numbers[i] , numbers[min_index] = numbers[min_index] , numbers[i]

print(numbers)

