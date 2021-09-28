# 1065번 한수
n=int(input())+1
h=0
for i in range(1,n):
    if i<100: h+=1
    else:
        num=list(map(int,str(i)))
        if num[1]-num[0]==num[2]-num[1]: h+=1
print(h)