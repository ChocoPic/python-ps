N = int(input())
cookie = []
for _ in range(N):
    cookie.append(input())
# print(cookie)

l_arm = r_arm = w = l_leg = r_leg = 0
heart_x = heart_y = 0
find_heart = 0
for x in range(len(cookie)):
    for y in range(len(cookie[x])):
        # 심장 찾기
        if find_heart==0 and cookie[x][y] == '*':
            heart_x = x+1
            heart_y = y
            # print(heart_x, heart_y)
            find_heart = 1
        # 길이 세기
        elif find_heart==1 and cookie[x][y]=='*':
            if x==heart_x :
                if y<heart_y: # 왼팔 길이 :심장 왼쪽(x동일)
                    l_arm += 1 
                elif y>heart_y: # 오른팔 길이: 심장 오른쪽(x동일)
                    r_arm += 1
            elif x>heart_x :
                if y==heart_y:  # 허리길이 : 심장 아래(y동일)
                    w += 1
                elif y<heart_y: # 왼다리 길이: 심장 왼쪽 아래
                    l_leg += 1
                elif y>heart_y: # 오른다리 길이: 심장 오른쪽 아래
                    r_leg += 1 
                
print(heart_x+1, heart_y+1)
print(l_arm, r_arm, w, l_leg, r_leg)