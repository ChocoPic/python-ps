'''
1 -+6-> 2~7 -+12-> 8~19 -+18-> 20~37
'''
N = int(input())
max_i = 1
answer = 1
while(True):
    if max_i>=N:
        print(answer)
        break
    max_i += 6*answer
    answer += 1