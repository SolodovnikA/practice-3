n = int(input())

hours = n // 30
minutes = (hours*5) + (n % 30) // 6

print(hours, minutes)
