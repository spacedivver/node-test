import sys
sys.stdin = open("input.txt", "r")

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    # arr=[[*map(int,input().split())] for _ in range(n)] # list함수를 사용하지 않고 대괄호 쓰면 * 붙여줘야함
    arr=[list(map(int,input().split())) for _ in range(n)] # * 붙이지 않고도 배열 값 제대로 출력
    arr_90=[[0 for _ in range(n)] for _ in range(n)]
    arr_180=[[0 for _ in range(n)] for _ in range(n)]
    arr_270=[[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            arr_90[i][j]=arr[n-1-j][i]
    
    for i in range(n):
        for j in range(n):
            arr_180[i][j]=arr_90[n-1-j][i]
    
    for i in range(n):
        for j in range(n):
            arr_270[i][j]=arr_180[n-1-j][i]
            
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(arr_90[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(arr_180[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(arr_270[i][j],end='')
        print()

