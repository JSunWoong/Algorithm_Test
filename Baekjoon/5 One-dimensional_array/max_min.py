# 10818 최대,최소
n=input()
lists=list(map(int,input().split()))
max=-1000000
min=1000000
for list in lists:
    max=list if list>max else max
    min=list if list<min else min
print(min,max)