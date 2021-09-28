# 4673 셀프넘버
num=set(range(1,10001))
const=set()
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    const.add(i)
for k in sorted(num-const):print(k)