numbers = [5, 3, 8, 1, 2]

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1 ):
        if numbers[j] > numbers[j+1]:
            numbers[j] , numbers[j+1] = numbers[j+1] , numbers[j]

print(numbers)