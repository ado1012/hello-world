mult = 1
sym = "*"
space = " "
count = int(input("Enter the number of rows (odd number):"))
while mult <= count :
    print(space * int((count - mult) /2) + sym*mult + space * int((count - mult) /2))
    mult += 2
