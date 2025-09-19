size, type = input("ขนาดและประเภท (เช่น M R): ").split()
top = input("ท็อปปิ้ง (N หรือ P 2 หรือ E 1): ").split()

price = 0

match size:
    case "S": price += 60
    case "M": price += 80
    case "L": price += 100
    case _:
        print("ขนาดไม่ถูกต้อง")
        exit()

match type:
    case "R": price += 0
    case "T": price += 20
    case _:
        print("ประเภทแป้งไม่ถูกต้อง")
        exit()

if top[0] == "N":
    price += 0
elif top[0] == "P":
    if len(top) >= 2 and top[1].isdigit():
        price += 15 * int(top[1])
    else:
        print("กรุณาระบุจำนวนท็อปปิ้ง P ให้ถูกต้อง")
        exit()
elif top[0] == "E":
    if len(top) >= 2 and top[1].isdigit():
        price += 20 * int(top[1])
    else:
        print("กรุณาระบุจำนวนท็อปปิ้ง E ให้ถูกต้อง")
        exit()
else:
    print("ประเภทท็อปปิ้งไม่ถูกต้อง")
    exit()

print(f"ราคา {price} บาท")

size,type = map(str,input().split())
top = map(str,input().split())
top = list(top)
price = 0
match size:
    case "S":price += 60
    case "M":price += 80
    case "L":price += 100
match type:
    case "R":price += 0
    case "T":price += 20
match top[0]:
    case "N":price += 0
    case "P":price += (15*int(top[1]))
    case "E":price += (20*int(top[1]))
print(f"ราคา {price} บาท")