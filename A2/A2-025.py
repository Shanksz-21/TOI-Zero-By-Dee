# Input
xAxis,yAxis = map(int,input().split())    # จำนวนตาราง
xBunn,yBunn = map(int,input().split())    # ตำแหน่งกระต่าย
nInfec = int(input())                     # จำนวนกระต่ายป่วย
infec = []                                # list ตำแหน่งของกระต่ายที่ป่วย
for i in range(nInfec):
      xInf,yInf = map(int,input().split())
      infec.append((xInf,yInf))

# เช็คโซนต่างๆ โดยไม่สนใจว่าซ้ำกันหรือไม่
redZone = []
yellowZone = []
safetyZone = []
for i in range(nInfec):
      xInfec = infec[i][0]
      yInfec = infec[i][1]
      for x in range(xAxis+1):
            for y in range(yAxis+1):
                  if xInfec-1 <= x <= xInfec+1 and yInfec-1 <= y <= yInfec+1:
                        redZone.append((x,y))
                  if xInfec-2 <= x <= xInfec+2 and yInfec-2 <= y <= yInfec+2:
                        yellowZone.append((x,y))
                  if not(xInfec-2 <= x <= xInfec+2) and not(yInfec-2 <= y <= yInfec+2):
                        safetyZone.append((x,y))
                        
# ตรวจสอบว่ามีตำแหน่งใดที่ซ้ำกัน
infec = set(infec)
redZone = set(redZone)
yellowZone = set(yellowZone)
safetyZone =set(safetyZone)
safetyZone = safetyZone.difference((yellowZone.union(redZone,infec)))
yellowZone = yellowZone.difference(redZone.union(infec))
redZone = redZone.difference(infec)
infec = list(infec)
redZone = list(redZone)
yellowZone = list(yellowZone)
safetyZone = list(safetyZone)

# ตรวจสอบความปลอดภัยของกระต่าย
dengerous = "0%"
P = 0
Ploop = len(infec)
while P < Ploop:
      if xBunn == infec[P][0] and yBunn == infec[P][1]:
            dengerous = "100%"
      P+=1
Q = 0
Qloop = len(redZone)
while Q < Qloop: 
      if xBunn == redZone[Q][0] and yBunn == redZone[Q][1]:
            dengerous = "60%"
      Q+=1
R = 0
Rloop = len(yellowZone)
while R < Rloop:
      if xBunn == yellowZone[R][0] and yBunn == yellowZone[R][1]:
            dengerous = "20%"
      R+=1
      
print(f"จำนวนพท.ปลอดภัย {len(safetyZone)} เขต")
print("ความเสี่ยงของน้อนต่าย:",dengerous)