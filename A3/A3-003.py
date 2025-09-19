N = int(input())
line1 = map(int, input().split())
line2 = map(int, input().split())
line1 = list(line1)
line2 = list(line2)
line1.insert(0,1)
line2.insert(0,1)
count = 0
for i in range(N):
    line1_Max = max(line1[i],line1[i+1])
    line1_min = min(line1[i],line1[i+1])
    line2_Max = max(line2[i],line2[i+1])
    line2_min = min(line2[i],line2[i+1])
    if line1_Max == line2_Max:
        if line1_min == line2_min:
            count += 1
    elif line2_min < line1[i] < line2_Max:
        if line1[i+1] != line2[i+1] != line2[i]:
            count += 1
    elif line1[i] == 1:
        if line2[i] == 2 and line2[i+1] == N or line2[i] == N and line2[i+1] == 2:
            count += 1
    elif line1[i] == N:
        if line2[i] == 1 and line2[i+1] == N-1 or line2[i] == N-1 and line2[i+1] == 1:
            count += 1
print(count)