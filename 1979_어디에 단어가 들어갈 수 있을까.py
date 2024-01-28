import sys
sys.stdin = open("input.txt", "r")

t=int(input())
for tc in range(1,t+1):
    n,k=map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)] # 배열 초기화
    find=0 # 정닶값
    for i in range(n):
        cnt=0 # 임시 체크 변수
        for j in range(n): # 가로의 경우 체크
            if arr[i][j]==1:
                cnt+=1
            if arr[i][j]==0 or j==(n-1): # 연속이 중단될 때, 끝자리에 도달했을 때
                if cnt==k: # 체크 개수가 단어 길이하고 같을 시
                    find+=1 # 정답값 추가
                cnt=0 # 다시 체크 개수 초기화

        for j in range(n): # 세로의 경우 체크
            if arr[j][i]==1:
                cnt+=1
            if arr[j][i]==0 or j==(n-1):
                if cnt==k:
                    find+=1
                cnt=0
    print('#%d %d'%(tc,find))
    
    