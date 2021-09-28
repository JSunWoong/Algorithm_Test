# 3052 나머지
count=1
lists=[]
for i in range(10):
    lists.append(int(input())%42)
for list in set(lists):
    if list!=lists[0]:
        count+=1
print(count)