def fact (n) :
    if n== 1 :
        return 1
    return n * fact(n-1)
print(fact(5))

def fib (n) :
    if n <= 1 :
        return n
    return fib(n-1) + fib(n-2)

for i in range(6) :
    print(fib(i))


def rev (text) :
    if len(text) <= 1 :
        return text
    return rev(text[1:]) + text[0]
print(rev("helloo"))
