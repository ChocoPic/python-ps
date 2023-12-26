'''
N개 / N-9개 / N-99개 / ... -> N - (10**i + 1)
'''

import sys
input = sys.stdin.readline
N = input().rstrip()
answer = 0
for i in range(1, len(N)):
    # 9 * 1 * 1자리 => 1~9
    # 9 * 10 * 2자리 => 10~19, 20~29, ... 99
    answer += 9 * 10**(i-1) * i #1~9 * 0몇개 * 그자리수
# (123(N)-100+1)*3자리 => 100 ~ 123
answer += (int(str(N)) - 10**(len(N)-1) +1) * len(N)    #몇개더 * 몇자리
print(answer)