t = int(input())

for tc in range(1,t+1):
    arr = list(input())
    l=len(arr)
    temp=0
    for i in range(l):
        if arr[i]!=arr[l-i-1]: # 인덱스가 l인 리스트 요소는 없음, 인덱스는 l-1까지 존재
            print('#%d 0'%tc)
            temp+=1
            break
    if temp==0:
        print('#%d 1'%tc)

# #================================================
# T = int(input())
#
# for t in range(1, T+1):
#     word = input()
#     for i in range(len(word)//2):
#         if word[i] == word[-1-i]:
#             answer = 1
#         else:
#             answer = 0
#     print("#{} {}".format(t, answer))
#
# #=================================================
#
# T = int(input())
# for test_case in range(1, T + 1):
#     word = input()
#     if word == word[::-1]: # [::-1]은 뒤에서 부터 데이터를 가져온다는것을 의미
#         print(f"#{test_case} 1")
#     else:
#         print(f"#{test_case} 0")
