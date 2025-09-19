N = int(input())
func = []
for _ in range(N):
    x,y = map(int,input().split())
    func.append((x,y))
result = []
for i in range(N):
    for j in range(i+1,N):
        dx = func[i][0]-func[j][0]
        dy = func[i][1]-func[j][1]
        if abs(dx) == abs(dy):
            result.append(abs(dx))
value_max = max(result)
print(value_max)