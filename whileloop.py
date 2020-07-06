#open file, read what's inside, if len <100, truncate, else add
#while inupt>100, truncate
filename = input("Please enter the file name --> ")
length = 0

with open(filename, "w+") as file:
    while True:
        line = input("Write your fav poem. -->" ) + "\n"
        if length + len(line) > 100:
            file.truncate()
            print ("Erasing the file")
            length = 0
        file.write(line)
        length += len(line)
