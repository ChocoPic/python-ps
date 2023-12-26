def solution(s):
    answer = ''
    i = 0   # 현재 단어에서의 인덱스
    for c in s:
        if c==' ':
            answer += ' '
            i = 0
        else: 
            answer += (c.upper() if i%2==0 else c.lower())
            i += 1
    return answer

def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))