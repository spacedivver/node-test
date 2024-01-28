# 2차원 배열 사용
t=int(input())
for t in range(1,t+1):
    n=int(input())
    # n_list=[[0]*i for i in range(1,n+1)] # 이거는 왜 안될까.....
    n_list=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j==0:
                n_list[i][j]=1
            else:
                n_list[i][j]=n_list[i-1][j-1]+n_list[i-1][j]
    print('#%d'%t)
    for i in range(n):
        for j in range(i+1):
            print(n_list[i][j],end=' ')
        print()
        
    

# n_list=[[0 for i in range(5)] for j in range(5)]
# arr=[[0]*2 for _ in range(5)]
# arr[0][0]=1
# print(arr)
# print(n_list)