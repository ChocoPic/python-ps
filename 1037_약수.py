# 진짜 약수: N은 A의 배수 && A는 1,N이 아님

# n=8 1 2 4 8
# n=2 1 2
# 가장 작은거랑 큰거랑 곱하면 됨
cnt = int(input())  # n의 진짜 약수 개수(1~50)
a = list(map(int, input().split()))    # n의 진짜 약수(2~1,000,000)
a.sort()
print(a[0] * a[-1])