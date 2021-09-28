# OX 퀴즈
n=int(input())
lists=[]
for i in range(n):
    lists.append(input())
for list in lists:
    score=cnt=0
    tmp=list[0]
    if tmp=='O': score+=1
    for s_list in list[1:]:
        if s_list=='O':
            score+=1
            if tmp==s_list:
                cnt+=1
                for i in range(cnt): score+=1
            tmp=s_list
        else:
            tmp=s_list
            cnt=0
    print(score)