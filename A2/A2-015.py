wide,long,layer = map(int,input().split())
price = int(input())
longAll = (2*wide) + (2*long)
priceAll = longAll*layer*price

print(f'{longAll}\n{priceAll}')