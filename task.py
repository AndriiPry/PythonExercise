#!/usr/bin/env python3
# -*-encoding: utf-8-*-

"""
A little program that allows user to do some usual things with filesystem.

The mainloop (infinite 'while' cycle) begins asking user which case to use:

    -c    Ask user for filename and create file with such name.
          If such file is already exists print an error message and continue
          (WARNING: this function shouldn't delete data from file in such case).

    -r    Ask user for filename and open file with such name for reading
          Ask user whether he wants to read entire file or just the first line.
          Print correspondent string and continue

    -w    Ask user for filename and open file with given name for writing.
          Begin an infinite loop. During each step ask user for string. If this
          string is not empty - write it to the file. Else - exit from cycle
          (using 'break') to the mainloop.

    -a    Ask user for filename and open file with given name for appending.
          Begin an infinite loop. During each step ask user for string. If this
          string is empty - exit from cycle. Othervise check whether result string
          has length less then MAX_SIZE variable. If it does then truncate it.
          Write string anyway.

    -s    Change MAX_SIZE value

    -q    End mainloop.

    -h    Print this prompt.
"""
import os.path
MAX_SIZE = 1000


while True:
  case = input("Enter your command  (-h for help).\n--> ")
  print("While loop has started")

  if case == '-c':
      filename = input("What would be the name the file? \n-->")
      if os.path.isfile(filename):
          print("Error: Such file already exists")
          continue
      with open(filename, "a") as file:
          pass

  elif case == '-r':
      filename = input("What would be the name the file? \n-->")
      with open(filename, "r") as file:
          ans = input("Entire file or just the first line? Press 'E' for entire or 'L' for the line \n--> ")
          if ans == "E":
              print(file.read())
          else:
              print(file.readline())

  elif case == '-w':
      filename = input("What would be the name the file? \n-->")
      with open(filename, "w") as file:
          while True:
              ans = input("Please type smth. Or leave it blank to quit \n--> ")
              if ans:
                  file.write(ans +"\n")
              else:
                  break
          # Begin an infinite loop. During each step ask user for string. If this
          # string is not empty - write it to the file. Else - exit from cycle
          # (using 'break') to the mainloop.

  elif case == '-a':
      filename = input("What would be the name the file? \n-->")
      with open(filename, "r") as file:
          length = len(file.read())
      with open(filename, "a") as file:
          while True:
              ans = input("Please type smth. Or leave it blank to quit \n--> ")
              if not ans:
                  break
              if lenght+len(ans) > MAX_SIZE:
                  file.truncate()
                  
#read into var -> while request line, add to var if doesn;t exceed maxsize
          # Ask user for filename and open file with given name for appending.
          # Begin an infinite loop. During each step ask user for string. If this
          # string is empty - exit from cycle. Othervise check whether result string
          # has length less then MAX_SIZE variable. If it does then truncate it.
          # Write string anyway.

  elif case == '-q':
    break
  elif case == '-h':
    print(__doc__)
  else:
    print("Bad command.")
