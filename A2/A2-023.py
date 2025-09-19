talk = str(input())
talk = talk.lower()
#case unknow
alpha_set = set(talk)
unit = len(talk)
if "t" and "i" in alpha_set and len(alpha_set) == 2:
    print(f"unknow {unit}")
else:
    pure_blood = ["ra","bi","bt"]
    i = 0
    status = True
    while i <= 3 and status:
# case unpure
        if i == 3:
            stat = True
            index_error = 0
            j = 0
            while j < unit-1 and stat:
                if talk[j] == "a":
                    if j == 0:
                        index_error = 0
                        status = False
                    elif talk[j-1] == "r":
                        continue
                    else:
                        index_error = j
                        stat = False
                else:
                    j += 1
            print(f"no {index_error}")
            status = False
# case pure
        elif pure_blood[i] in talk:
            unit_a = ["a" * k in talk for k in range(1, unit + 1)]
            unit_a = unit_a.count(True)
            print(f"yes {unit_a}")
            status = False
        i += 1