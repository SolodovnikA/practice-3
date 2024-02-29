x = int(input())
y = int(input())
n = int(input())
total = n * (x + (y * 0.01))
totalr = total // 1
totalk = (total*100)%100
print(totalr, 'руб.', totalk, 'коп.')
