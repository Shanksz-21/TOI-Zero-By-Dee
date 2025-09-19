inject = str(input())
total = len(inject)
if "buu" in inject.lower():
    count = inject.lower().count("u")
    print(f"YES {count}")
else:
    index = inject.lower().find("b")
    print(inject[:index+1],end='')
    print("U"*(total-index-1))