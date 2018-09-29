rows = int(input("pascal triangle size: "))
what = [1]
for i in range(rows):
    print(what)
    ughh = []
    ughh.append(1)
    for z in range(len(what)-1):
        ughh.append(what[z] + what[z+1])
    ughh.append(1)
    what = ughh
