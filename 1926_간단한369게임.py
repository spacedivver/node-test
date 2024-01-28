n = int(input())
number = ['3', '6', '9']
for i in range(1, n+1):
  num = (str(i)) # 각 자리수 문자열 치환
  clap = 0
  for j in range(len(num)): #숫자의 자리수 마다
    if num[j] in number: # number리스트 숫자들이 있는지 확인
      clap += 1
  if clap > 0:
    num = '-' * clap #박수 횟수 만큼 '-'
  print(num, end=' ')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    if i >= 1 and i <= 10:
        temp=0
        if i%3==0:
            print('-',end=' ')
            temp+=1
        if temp==0:
            print(i,end=' ')
    elif i>10 and i<=100:
        temp=0
        a=i%10
        b=i//10
        if b%3==0:
            print('-',end=' ')
            temp+=1
        if a%3==0 and a!=0:
            print('-',end=' ')
            temp+=1
        if temp==0:
            print(i,end=' ')
    elif i>100 and i<=1000:
        temp=0
        a=i%10
        b=(i%100)//10
        c=i//100
        if c%3==0:
            print('-',end=' ')
            temp+=1
        if b%3==0 and b!=0:
            print('-',end=' ')
            temp+=1
        if a%3==0 and a!=0:
            print('-',end=' ')
            temp+=1
        if temp==0:
            print(i, end=' ')





# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for i in range(1, T + 1):
#     if i >= 1 and i <= 10:
#         temp=0
#         if i%3==0:
#             print('-',end=' ')
#             temp+=1
#         if temp==0:
#             print(i,end=' ')
#     elif i>10 and i<=100:
#         temp=0
#         a=i%10
#         b=i//10
        
#         if a%3==0 and a!=0:
#             if b%3==0:
#                 print('--',end=' ')
#                 temp+=1
#             else:
#                 print('-',end=' ')
#                 temp+=1
#         elif b%3==0:
#             print('-',end=' ')
#             temp+=1
        
#         if temp==0:
#             print(i,end=' ')
            
#     elif i>100 and i<=1000:
#         temp=0
#         a=i%10
#         b=(i%100)//10
#         c=i//100
#         if a%3==0 and a!=0:
#             if b%3==0:
#                 if c%3==0:
#                     print('---',end=' ')
#                     temp+=1
#                 else:
#                     print('--',end=' ')
#                     temp+=1
#             else:
#                 print('-',end=' ')
#                 temp+=1
#         elif a%3!=0:
#             if b%3==0 and b!=0:
#                 if c%3==0:
#                     print('--',end=' ')
#                     temp+=1
#                 else:
#                     print('-',end=" ")
#                     temp+=1
#             else:
#                 print(i,end=' ')
#         else:
            
#             print(i,end=' ')
            

