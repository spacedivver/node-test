import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1,t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    # 가로, 세로 값 검사
    for i in range(9):
        cnt_r = [0] * 10
        cnt_c = [0] * 10
        
        for j in range(9):
            # 스도쿠 안의 숫자는 1부터 시작함으로 인덱스를 10까지 설정
            cnt_r[arr[i][j]] += 1
            cnt_c[arr[j][i]] += 1

        # 중복 여부 체크
        for k in range(1, 10):
            if cnt_r[k] != 1:
                result = 0
                break
            if cnt_c[k] != 1:
                result = 0
                break

    # 3x3 격자 자리 중복 검사
    for i in range(3):
        for j in range(3):
            cnt_x = [0] * 10
            for k in range(3):
                for l in range(3):
                    cnt_x[arr[3*i+k][3*j+l]] += 1

            for k in range(1, 10):
                if cnt_x[k] != 1:
                    result = 0
                    break

    print('#%d %d'%(tc,result))
    # print("#{} {}".format(tc, result))


t = int(input()) # TC 갯수
for k in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(9)] # 2차원 배열 입력
    rowArr = arr #가로 배열은 입력받은 배열과 동일
    colArr = [[arr[i][j] for i in range(9)] for j in range(9)] #세로 배열 변환
    sqrArr = [[arr[i % 3 * 3 + j // 3][i // 3 * 3 + j % 3] for j in range(9)] for i in range(9)] # 3 * 3 사각형 각각을 1차원 배열로 변환
    answer = 1 #출력할 정답
    for row, col, sqr in zip(rowArr, colArr, sqrArr): # 2차원배열에서 각각 1차원 배열을 꺼내서
        if len(set(row)) == len(set(col)) == len(set(sqr)) == 9: # 집합으로 변환했을때 길이가 모두 9이면 
            continue # 통과
        else: #아니면 (스도쿠 조건 충족 X)
            answer = 0 #정답 0으로 설정
            break # 반복 중단
    print("#", k, " ", answer, sep="") #정답 출력


# import sys
# sys.stdin = open("input.txt", "r")

# t=int(input())
# for tc in range(1,t+1):
#     arr=[list(map(int,input().split())) for _ in range(9)]
#     temp=[]
#     chk=0
#     for i in range(9):
#         for j in range(9):
#             if arr[i][j] in temp:
#                 chk+=1
#             temp.append(arr[i][j])
#         temp=[]
        
#         for j in range(9):
#             if arr[j][i] in temp:
#                 chk+=1
#             temp.append(arr[j][i])
#         temp=[]
        
#     for i in range(0,9,3):
#         for x in range(i):
#             for y in range(i):
#                 if arr[x][y] in temp:
#                     chk+=1
#                 temp.append(arr[i][j])
                
#     if chk>=1:
#         print('#%d 0'%tc)
#     else:
#         print('#%d 1'%tc)