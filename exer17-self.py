from sys import argv
from os.path import exists

# request input and output file names

script, from_file, to_file = argv

# open input file, save content of the file to a variable
inputfile = open(from_file, 'a')
new_text = input("Type the text you want to add. Otherwise press Enter. \n--> ")
inputfile.write(new_text +"\n")
inputfile = open(from_file, 'r')
inputfiletext = inputfile.read()
print(inputfiletext)

answer = input("Do you want to close or truncate the file? \n--> ")
if answer == "close":
    inputfile.close()
    print("Closing the file")
elif answer == "truncate":
	inputfile = open(from_file, 'w')
	print("Truncating the file")
else:
	print("This is a wrong command")

# check whether input and output files exist
print(f"Checking whether {to_file} exists. --> {exists(to_file)}")

# open out file, copy input content there
outputfile = open(to_file, 'w')
outputfile.write(inputfiletext)

print(f"Here's what is in the {to_file}")
outputfile = open(to_file, 'r')
outputfiletext = outputfile.read()
print(outputfiletext)

# close both files

print("Now we're closing both files")
inputfile.close()
outputfile.close()