n = int(input())
bun = []
for i in range(0,n):
    name,weight = map(str,input().split())
    bun.append([name,int(weight)])
weight_list = []
count = 0
weightMax = 0
for j in range(0,n):
    if bun[j][1] > 15:
        count += 1
    if bun[j][1] > weightMax:
        weightMax = bun[j][1]
        weight_list = bun[j]
print(count)
print(weight_list[0],weight_list[1])