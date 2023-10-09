#a의 약수 c : a=bc
# f(a) : a 약수들 합
# g(a) : a이하 수들의 약수들의 합
'''
f(1) = 1
f(2) = 1 + 2
f(3) = 1 + 3
f(4) = 1 + 2 + 4
f(5) = 1 + 5
g(5) = 1*5 + 2*2 + 3*1 + 4*1 + 5*1
=> g(n) = 1*n + 2*(n//2) + 3*(n//3)+...n*(n//n)
n이하수중에 i로나눠지는 수 개수들 합(1<=i<=n)
'''
n = int(input())
answer = 0

for i in range(1, n+1):
   answer += i*(n//i)
print(answer)