import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if nums[i-1] > nums[i]:    #뒤부터 탐색. 내림차순 시작지점찾기
        for j in range(N-1, i-1, -1):
            if nums[i-1] > nums[j]:   #[i:]에서 직전 작은수 찾기
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = sorted(nums[i:], reverse=True)
                print((' ').join(map(str,nums)))
                exit()
print(-1)