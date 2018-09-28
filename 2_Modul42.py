num = []
x = []

for i in range(1, 11):
    num.append(int(input("input number (u'll be askd 10 times) ")))
for i in num:
    x.append(int(i) % 42)
z = (dict((y,x.count(y)) for y in set(x)))

print(len(z.keys()))
