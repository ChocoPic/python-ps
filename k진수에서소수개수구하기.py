def to_k(n, k):
    result = ''
    while n:
        result = str(n%k) + result
        n //= k
    return result

def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    for num in to_k(n, k).split('0'):
        if num != '' and is_prime(int(num)):
            answer += 1
    return answer


'''
수 
...
= qxp
= rxr -----기준-----
= pxq
...
=> 제곱근까지만 나눠보면 됨.
'''