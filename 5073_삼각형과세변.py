while(True):
    tri = list(map(int, input().split()))
    if tri[0]==0 and tri[0]==0 and tri[0]==0:
        break
    tri.sort()
    if tri[2] >= tri[0]+tri[1]:
        print("Invalid")
    else:
        if tri[0]==tri[1] and tri[1]==tri[2] and tri[0]==tri[2]:
            print("Equilateral")
        elif tri[0]!=tri[1] and tri[1]!=tri[2] and tri[0]!=tri[2]:
            print("Scalene")
        else:
            print("Isosceles")