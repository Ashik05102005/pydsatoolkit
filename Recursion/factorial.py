def fact_iter(n) :
    res = 1
    for i in range(1 , n + 1) :
        res *= i
    return res
print(fact_iter(5))
# recursive 
def fact(n) :
    if n == 1 :
        return 1 
    return n * fact(n-1)

print(fact(6))

