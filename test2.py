from sys import argv
_, filename = argv


with open(filename, "a") as file:
    file.write(input("Please add your message. -->  ") + "\n")



with open(filename, "r") as file:
    a = file.read()
    print(a)


#
# print(filename)
# file = open(filename, "r")
# file



# print(f"We'll erase the {filename} first. \n If you don't want this, press CTRL-C (^C) \n If you do want this, hit RETURN")
#
# input ("?")
#
# print ("Opening the file")
# txt = open(filename,'w')
#
# print(f"Trunkating {filename}")
# txt.truncate()
#
# print("Now please write smth")
#
# line1 = input("Line 1 =>")
# line2 = input("Line 2 =>")
# line3 = input("Line 3 =>")
#
# txt.write(line1)
# txt.write("\n")
# txt.write(line2)
# txt.write("\n")
# txt.write(line3)
#
# print("And finally we close the file")
# txt.close()
