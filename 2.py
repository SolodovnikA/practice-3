initial_sec = int(input('Введите целое число от 1 до 86400: '))
hours = initial_sec // 3600
minutes = (initial_sec % 3600) // 60
sec = (initial_sec % 3600) % 60
print(hours, ':', minutes, ':', sec)
