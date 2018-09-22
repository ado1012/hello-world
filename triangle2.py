mult = 1
sym = "*"
space = " "
count = int(input("Enter the number of rows:"))
while mult <= count :
    print(space * (count - mult) + sym*mult)
    mult += 1
