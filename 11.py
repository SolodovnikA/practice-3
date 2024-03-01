import math as m

a = int(input())
b = int(input())
c = int(input())

alpha = m.degrees(m.acos((a**2+b**2-c**2)/(2*a*b)))
beta = m.degrees(m.acos((a**2+c**2-b**2)/(2*a*c)))
gamma = m.degrees(m.acos((b**2+c**2-a**2)/(2*b*c)))

print(alpha, beta, gamma)
