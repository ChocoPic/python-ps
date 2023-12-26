def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i in range(len(citations)):
        if citations[i] > h_index:   #i번째로 많이인용된 논문 인용횟수(=h번 안용된 논문) i편 이상 > 이전까지 논문개수
            h_index = i+1
        else:
            break
    return h_index        
# h편 이상 인용된 논문이 h편 이상이면, 이때 h의 최댓값