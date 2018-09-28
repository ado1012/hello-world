name = input("write your full name: ")
nameReplacer = name.replace("-", " ")
nameList = nameReplacer.split()
def initials (name_list):
    for i in name_list:
        print(i[0].upper(), end = "")
initials(nameList)
