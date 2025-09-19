N = int(input())
num_list = []
for i in range(N):
    n = int(input())
    num_list.append(n)
unit = []
for j in range(N):
    x = num_list[j]
    count = num_list.count(x)
    unit.append(count)
unitMax = max(unit)
print(unitMax)