# 1 11 111 1111 11111
# 배수를 1 11...로 나눠서 0이면 답이다. 배수 == 나누어떨어짐

# 1로된 숫자 만들기 : 이전거*10 + 1
# 1로된 숫자가 n으로 나누어 떨어지면
# i를 출력

while True:
    # 입력받기. 종료 조건이 없으니 try except로 종료되게 함
    try:
        n = int(input())    #1~10000 정수
    except:
        break
    
    num = 0  # 1로만 이루어진 숫자
    i = 0  # 자리수
    while True:
        num = num*10 + 1    #1,11,111...
        i += 1
        if num%n == 0:
            print(i)
            break   