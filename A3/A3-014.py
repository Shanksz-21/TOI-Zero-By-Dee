N = int(input())
hourList = []
for _ in range(N):
    H = int(input())
    hourList.append(H)
hourBig = 0
hour = len(hourList)
for i in range(N):
    if hourList[i]>18:
        hourBig += 1
    else:
        continue
hour -= hourBig     #ลบค่าที่ซ้ำ
hour -= hourBig-1   #เติมค่าในช่องว่าง เช่น 20 ... 22 ... 19
if hour <= 0:
    result = 2*hourBig-1
    print(result)
else:
    result = hour + hourBig
    print(result)