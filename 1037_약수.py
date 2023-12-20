def solution(coin, cards):
    answer = 1
    index = 0 
    n = len(cards)
    my_cards = cards[:n//3]

    while index<=n-1:
        # 라운드시작
        print(my_cards)

        # 1) 갖고 있는 카드 중에 합이 n+1이 되는 게 있으면, 카드를 내고 다음 라운드로
        flag = 0    # 갖고 있는 카드 중에 냈는지
        for i in range(len(my_cards)):
            a = my_cards[i]
            for j in range(len(my_cards)):
                c = my_cards[j]
                if (a!=c) and (a+c==n+1):
                    my_cards.remove(c)
                    my_cards.remove(a)
                    flag = 1
                    break
            if flag == 1:
                break

        # 2) 없으면 카드를 2장 뽑습니다.
        if flag == 0:
            new_card1 = cards[index]
            new_card2 = cards[index+1]
            index += 2
        
            if coin > 1:     # coin이 1개이상 있으면 카드를 뽑고 버립니다.
                for k in range(len(my_cards)):
                    c = my_cards[k]
                    if (new_card1+c)==n+1 and coin>1:
                        coin -= 1
                        my_cards.remove(c)
                        break
                    
                for k in range(len(my_cards)):
                    c = my_cards[k]
                    if (new_card2+c)==n+1 and coin>1:
                        coin -= 1
                        my_cards.remove(c)
                        break
                
        answer +=1
        
    return answer
print(solution(4, [3,6,7,2,1,10,5,9,8,12,11,4]))