def winner():
    if num_of_stones % 2 == 1:
        print("alice")
    else:
        print("bob")
while True:
    num_of_stones = int(input("how many stones u want fam?: "))
    winner()
