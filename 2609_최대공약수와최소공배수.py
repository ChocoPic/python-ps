def gcd(a, b):  #나머지가 0이 될 때 까지
    if b==0:
        return a
    else:
        return gcd(b, a%b)

# def find_gcd(a, b):
#     gcd = 1

#     for i in range(2, min(a,b)+1) :	#둘 중 작은 수까지만 계산해보면 됨
#         if a%i==0 and b%i==0:	# 두 수가 동시에 나누어 떨어지는 경우
#             gcd = i
#     return gcd

def lcm(a, b):  # gcd*lcm = a*b
    return (a*b//gcd(a,b))

n = list(map(int, input().split()))
n.sort()
print(gcd(n[1],n[0]))
print(lcm(n[1],n[0])) 

# print(find_gcd(n[1], n[0]))