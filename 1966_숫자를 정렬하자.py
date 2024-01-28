import sys
sys.stdin = open("input.txt", "r")

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    # arr.sort()
    for i in range(n-1,0,-1): # n-1부터 0까지 -1씩 감소하면서
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    # print("#{}".format(tc))
    print(f"#{tc}",end=' ')
    print(*arr)