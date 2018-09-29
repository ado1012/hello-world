rows = int(input("pascal triangle size: "))
list1 = [1]
for i in range(rows):
    print(list1)
    newlist = []
    newlist.append(1)
    for z in range(len(list1)-1):
        newlist.append(list1[z] + list1[z+1])
    newlist.append(1)
    list1 = newlist
