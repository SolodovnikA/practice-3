att = int(input())
comp = int(input())
yds = int(input())
td = int(input())
int_ = int(input())

frst = (comp/att)-0.3
scnd = (yds/att)-3
thrd = (td/att)*20
frth = (int_/att)*25

numerator = (frst*5) + (scnd*0.25) + thrd + 2.375 - frth

print((numerator/6)*100)
