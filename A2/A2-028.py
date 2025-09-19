unit = int(input())
p1 = str(input())
p2 = str(input())
collumP = []
if unit == len(p1) == len(p2):
      for collum in range(unit):
            if int(p1[collum])+int(p2[collum]) == 9:
                  collum+=1
            else:
                  collumP.append(collum+1)
      if len(collumP) > 0:
            print("NO")
            for i in range(len(collumP)):
                  print(collumP[i],end=" ")
      else:
            print("YES")
else:
      print("จำกัดความยาวตามข้อมูลจามที่คุณกำหนด",unit)