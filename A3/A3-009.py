N,K = map(int,input().split())
num = []
for n in range(N):
    p = int(input())
    num.append(p-1)
pod = [0 for i in range(K)]
for i in range(K):
    for j in range(N):
        if num[j] == i:
            pod[i] += 1
min_pod = min(pod)
for k in range(K):
    pod[k] -= min_pod
print(sum(pod))