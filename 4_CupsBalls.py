moves = str(input("choose the combo (a/b/c). dont type anything else. "))
list = ["b"," "," "]
for i in range (len(moves)):
    if moves[i] == "a":
        temporary = list[0]
        list[0] = list[1]
        list[1] = temporary
    elif moves[i] == "b":
        temporary = list[1]
        list[1] = list[2]
        list[2] = temporary
    elif moves[i] == "c":
        temporary = list[0]
        list[0] = list[2]
        list[2] = temporary
    else:
        print("i said DONT TYPE ANYTHING OTHER THAN A/B/C")
print(list)
for j in range(3):
    if list[j] == "b":
        print("the ball is in ", j+1)
