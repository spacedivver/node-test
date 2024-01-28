# import sys
# sys.stdin = open("input.txt", "r")

t=int(input())

for tc in range(1,t+1): # 테스트 케이스 숫자 바꾸는 거 잊지말자
    arr=list(map(int,input().split()))
    arr.sort()
    n=len(arr)
    sum=0
    for i in range(1,n-1):
        sum+=arr[i]
    avg=sum/(n-2) # 정신 안차리니... len은 함수잖아.... 변수가 아니라...
    print('#%d %d'%(tc,round(avg)))
    
    
# 반올림 함수는 round()
# 1의 자리 반올림 round(num,-1), 10의 자리 방향으로 두번째 인자 -1씩 내림
# 소수 첫번째 자리 반올림 round(num)
# 소수 두번째 자리 반올림 round(num,1), 소수 세번째 자리 방향으로 두번째 인자 1씩 올림
# 사사오입 원칙 적용, 반올림 자리의 수가 5이면 앞자리가 짝수이면 내림, 홀수이면 올림