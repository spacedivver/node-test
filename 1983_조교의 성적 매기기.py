import sys
sys.stdin = open("input.txt", "r")

t=int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1,t+1):
    n,k=map(int,input().split())
    temp=0
    arr=[] # for문 외부에 위치시 실행 오류
    for i in range(n):
        # arr=[[*map(int,input().split())] for _ in range(n)]
        m,l,h=map(int,input().split())
        sum=m*0.35+l*0.45+h*0.2
        arr.append(sum)
    k_score=arr[k-1]
    
    arr.sort(reverse=True)
    d=n//10 # 학생 수에 따라 나누는 간격 조정
    g_index=arr.index(k_score)//d
    print('#%d %s'%(tc,grades[g_index]))


# sort옵션
# reverse() - 거꾸로 뒤집기, desc와 다름
# sort(reverse=True) - 내림차순
# sort() - 오름차순
# sorted() - 순서대로 정렬, 본체 변형 x
# ex) x=[1,2,3], y=sorted(x)
# reversed() - 거꾸로 뒤집기, 확인 위해서 list로 변형 필요
# ex) x=[1,2,3], y=reversed(x), list(y)

            
#010 4981 7049
# 나중에 리스트 초기화하는 부분도 적어보기