N,S = map(int, input().split())
mList = []
for _ in range(N):
    a = int(input())
    mList.append(a)
st1 = [0]
nd2 = [0]
rd3 = []
for i in range(N):
    if mList[i]%3==0 and mList[i]%4!=0:
        a = (2 * 5 * mList[i]) / 3
        st1.append(a)
    elif mList[i]%4==0 and mList[i]%3!=0:
        b = (2 * 5 * mList[i]) / 4
        nd2.append(b)
    elif mList[i]%3==0 and mList[i]%4==0:
        a = (2 * 5 * mList[i]) / 3
        b = (2 * 5 * mList[i]) / 4
        rd3.extend([a,b])
if len(rd3)==0:
    result = S-(sum(st1)+sum(nd2))
else:
    for j in range(len(rd3)):
        result = S-(sum(st1)+sum(nd2)+rd3[j])
        print(result,end=' ')