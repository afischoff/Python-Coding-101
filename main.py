"""
This program allows the user to easily run Python scripts in different directories from the command line.
This is useful for development in modern web based IDEs, since they are designed for running applications
which begin from the main.py file.

usage: $ python main.py
"""

# import packages
import os
import time


def showDirectories():
  """
  Prints the current directories to the console and returns a list of directories
  :return: List
  """
  # create list of directories
  directories = []
  for dirname, dirnames, filenames in os.walk('.'):
    if dirname[2:3] == '.' or dirname == '.':
      continue

    directories.append(dirname)

  # sort and loop through directories and display each one
  directories.sort()
  for num, name in enumerate(directories, start=1):
    print("{}) {}".format(num, name))

  return directories

def showFiles(dirs):
  """
  Prints the files in the given directory to the console and returns a list of files
  :param dirs: List
  :return: List
  """
  # sort and gather files from selected directory
  filenames = None
  for dirname, dirnames, filenames in os.walk(dirs[int(dirNum) - 1]):
    if len(filenames) == 0:
      print('Empty directory')
      print('----------')
      break

    num = 1
    filenames.sort()
    for filename in filenames:
      print("{}) {}".format(num, filename))
      num += 1

  return filenames


"""
This is the main program which runs in a continuous loop, pausing at the end of each iteration.
"""
while True:
  # display directory options
  directories = showDirectories()

  # ask user for directory
  print('Enter a directory number: (or q to quit)')
  dirNum = input()

  # break from the loop if the user enters a 'q'
  if dirNum == 'q':
    break

  print('----------')

  # display file options
  filenames = showFiles(directories)
  if len(filenames) == 0:
    continue

  # ask user for selected file
  print('Enter a file number:')
  fileNum = input()

  # execute the file
  print('----------')
  exec(open(directories[int(dirNum) - 1] + '/' + filenames[int(fileNum) - 1]).read())
  print('----------')

  # pause for 3 seconds before looping again
  time.sleep(3)