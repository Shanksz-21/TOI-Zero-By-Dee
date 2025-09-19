color,unit = map(str,input().split())
unit = int(unit)

rgb = ["red","green","blue"]
match color:
    case "red":
        for i in range(unit):
            if i % 3 == 0:
                print(rgb[0], end=" ")
            if i%3 == 1:
                print(rgb[1],end=" ")
            elif i%3 == 2:
                print(rgb[2],end=" ")
    case "green":
        for i in range(unit):
            if i % 3 == 0:
                print(rgb[1], end=" ")
            if i % 3 == 1:
                print(rgb[2], end=" ")
            elif i % 3 == 2:
                print(rgb[0], end=" ")
    case "blue":
        for i in range(unit):
            if i % 3 == 0:
                print(rgb[2], end=" ")
            if i%3 == 1:
                print(rgb[0],end=" ")
            elif i%3 == 2:
                print(rgb[1],end=" ")