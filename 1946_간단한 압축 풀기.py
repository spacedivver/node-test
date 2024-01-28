import sys
sys.stdin = open("input.txt")

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    value = ""
    for i in range(n) :
        C, K = input().split()
        K = int(K)
        value += C*K # 문자열 한 줄로 먼저 생성
        
    print("#{}".format(tc))
    for i in range(len(value)) :
        if (i+1)%10 == 0 : # 10번째 값이면 출력하고 줄 바꿈
            print(value[i])
        else :
            print(value[i], end="")
    print()