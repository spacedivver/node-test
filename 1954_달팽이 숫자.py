import sys
sys.stdin = open("input.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    dist = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우, 하, 좌, 상
    snail = [[0] * n for _ in range(n)] # 0으로 채워진 n*n 빈달팽이 생성
    num = 1 # 달팽이를 채울 숫자
    d = 0 # 달팽이 이동방향
    x, y = 0, -1 # 시작위치
    while num <= (n*n):
        nx, ny = x + dist[d][0], y + dist[d][1]
        if 0 <= nx < n and  0<= ny < n and snail[nx][ny] == 0 :
            snail[nx][ny] = num # 숫자 넣어주기
            num += 1 # 숫자 증가
            x, y = nx, ny # 현재 위치 갱신
            
        # 달팽이 크기에서 벗어났거나, 해당 위치에 이미 숫자가 부여되어 있는 경우
        # k값 조정을 통해 방향을 바꾼다.
        else:
            d = (d+1) % 4 # 0, 1, 2, 3 으로만 움직일 수 있게 나머지를 구함
    print(f"#{test_case}")
    for row in snail:
        print(*row)


# T = int(input())

# # row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# for tc in range(1, T+1):
#     N = int(input())
#     snail = [[0]*N for _ in range(N)]
#     # 초기 위치 & 회전방향 설정
#     r, c = 0, 0
#     dist = 0  # 0:우, 1:하, 2:좌, 3:상

#     for n in range(1, N*N + 1):
#         snail[r][c] = n
#         r += dr[dist]
#         c += dc[dist]

#         # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 체인지
#         # 근데 이런 경우라면 요소 인덱스를 다시 원위치시켜줘야하므로 빼줘야함
#         # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직일 수 있도록 행렬 인덱스 업데이트
#         if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
#             # 실행취소
#             r -= dr[dist]
#             c -= dc[dist]
#             # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
#             dist = (dist + 1) % 4
#             #  다시 gogo
#             r += dr[dist]
#             c += dc[dist]

#     print("#{}".format(tc))
#     for row in snail:
#         print(*row)
#     print()