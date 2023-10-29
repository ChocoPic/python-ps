'''
이기려면? 1을 남겨야함
2남기면 -> S1, C1 :SK
3-> S1,C1,S1 :CY
4-> S3,C1 :SK
5-> S3,C1,C1 :CY
6-> S3,C1,S1,C1 :SK
'''
N = int(input())
if N%2==0:
    print("CY")
else:
    print("SK")