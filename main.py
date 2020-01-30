import os
import time

# keep the program running
while True:
  # create list of directories
  directories = []
  for dirname, dirnames, filenames in os.walk('.'):
    if dirname[2:3] == '.' or dirname == '.':
      continue

    directories.append(dirname)

  # loop through directories and display each one
  for num, name in enumerate(directories, start=1):
      print("{}) {}".format(num, name))

  # ask user for directory
  print('Enter a directory number: (or q to quit)')
  dirNum = input()

  # break from the loop if the user enters a 'q'
  if (dirNum == 'q'):
    break

  print('----------')

  # gather files from selected directory
  for dirname, dirnames, filenames in os.walk(directories[int(dirNum) - 1]):
    num = 1
    for filename in filenames:
      print("{}) {}".format(num, filename))
      num += 1

  # ask user for selected file
  print('Enter a file number:')
  fileNum = input()

  # execute the file
  print('----------')
  exec(open(directories[int(dirNum) - 1] + '/' + filenames[int(fileNum) - 1]).read())
  print('----------')

  # pause for 3 seconds before looping again
  time.sleep(3)
