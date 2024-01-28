import sys
sys.stdin = open("input.txt", "r")

t=int(input())
for tc in range(1,t+1):
    h=0
    m=0
    h1,m1,h2,m2=map(int,input().split())
    h=h1+h2
    m=m1+m2
    if m>=60:
        h+=1
        m=m%60
    
    if h>12:
        if h%12==0:
            h=12
        else:
            h=h%12
    print('#%d %d %d'%(tc,h,m))