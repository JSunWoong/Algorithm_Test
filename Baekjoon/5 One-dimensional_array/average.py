# 1546 평균
n=int(input())
subs=[]
subs=list(map(int,input().split()))
sum=0
for i in range(len(subs)):
    sum += subs[i]/max(subs)*100
print(sum/n)