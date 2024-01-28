import sys
sys.stdin = open("input.txt", "r")

t=int(input())
for t in range(1,t+1):
    n=int(input())
    money=[50000,10000,5000,1000,500,100,50,10]
    list=[0]*8
    for i in range(8):
        if n//money[i]!=0:
            list[i]=n//money[i]
            n=n%money[i]
    print("#{}".format(t))
    print(*list)

