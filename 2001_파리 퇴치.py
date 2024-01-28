# import sys
# sys.stdin = open("input.txt", "r")

t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    max=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp=0
            for k in range(m):
                for l in range(m):
                    temp+=arr[i+k][j+l]
                    if max<temp:
                        max=temp
    print('#%d %d'%(tc,max))
    
    
    # for i in range(m):
    #     for j in range(m):
    #         print(arr[i][j])
    #     print()