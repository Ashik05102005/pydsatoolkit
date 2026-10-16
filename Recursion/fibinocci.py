# recursive

def fib(n) :
    if n <= 1 :
        return n 
    return fib(n - 1) + fib(n - 2)

for num in range(7) :
    print(fib(num) , end=" | " )

print("")
# iterative 

def fib(n):
   
   a , b = 0 ,1
   for _ in range(n):
       print(a , end=" | ")
       a , b  = b , a + b

fib(5)


