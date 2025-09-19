L,N = map(int,input().split())
position = []
for i in range(N):
    x1,x2 = map(int,input().split())
    position.append((x1,x2))
try:
    if L > 300 or N > 300 or L < 1 or N < 1:
        raise ValueError
except ValueError:
    print("ValueError")
else:
    count = 0
    count_list = []
    for x1,y1 in position:
        for x2,y2 in position:
            if x2 < x1 < y2:
                count += 1
            count_list.append(count)
        count = 0
gap = max(count_list)+1
print(gap)