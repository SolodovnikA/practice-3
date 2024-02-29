x = int(input())
y = int(input())

print(min(((x % y)+1), ((y % x)+1)))
