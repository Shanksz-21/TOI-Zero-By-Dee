N = int(input())
disList = []
for _ in range(N):
    dis = int(input())
    disList.append(dis)
disList.sort()
sum_dis = []
for i in range(N):
    sum_ = sum(disList[:i+1])
    sum_dis.append(sum_)
sum_dis = sum_dis * 2
res = sum(sum_dis)
print(res)