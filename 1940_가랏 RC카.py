import sys
sys.stdin = open("input.txt")

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    d=0
    v_RC=0
    for i in range(n):
        arr=list(map(int,input().split()))
        if arr[0]==0:
            d+=v_RC
        elif arr[0]==1:
            v_RC+=arr[1]
            d+=v_RC
        elif arr[0]==2:
            if v_RC>arr[1]:
                v_RC-=arr[1]
                d+=v_RC
            else:
                v_RC=0
            
    print("#{} {}".format(tc, d))