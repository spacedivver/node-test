# 2007. 패턴 마디의 길이
t=int(input())
chk=0
len=0
cnt=0
for i in range(t):
    n_list=input()
    len=n_list.length()
    for j in range(len):
        if n_list.count(n_list[j])!=0:
            chk=n_list[j-1]
            break
    for k in range(len):
        if chk==n_list[k]:
            cnt+=1
    print("#%d %d"%(t+1,cnt))
