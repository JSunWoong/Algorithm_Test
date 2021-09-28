# 4344 평균은 넘겠지
for _ in range(int(input())):
    ll=list(map(int,(input().split())))
    avg=sum(ll[1:])/ll[0]
    ratio=0
    for score in ll[1:]:
        if avg<score: ratio+=1
    print(f"{ratio/ll[0]*100:.3f}%")