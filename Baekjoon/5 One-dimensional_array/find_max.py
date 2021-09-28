# 2562 최댓값
list=[]
c=a=0
for i in range(9):
    n=int(input())
    list.append(n)
print(max(list))
print(list.index(max(list))+1)