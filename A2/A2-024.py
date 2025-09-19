L,P = map(int, input().split())
rabbit,monkey,frog = map(int, input().split())
po_list = []
for i in range(P):
    pos,poi = map(int, input().split())
    po_list.append((pos,poi))
l = [rabbit,monkey,frog]
animal = [0,0,0]
for p in range(3):
    for q in range(P):
        if po_list[q][0] % l[p] == 0:
            animal[p] += po_list[q][1]
scoreMax = max(animal)
Animal = ["rabbit","monkey","frog"]
for j in range(3):
    if scoreMax == animal[j]:
        print(f"{Animal[j]} {scoreMax}")