def solution(n):
    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[i-2] + fib[i-1])
    return fib[n]%1234567       

def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a,b = b, a+b
    return a