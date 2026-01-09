###########################
###########################
# List files in directory #
###########################
###########################

# import OS module
import os
# Get the list of all files and directories
path = "C://Users//Vanshi//Desktop//gfg"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)

import os
print("Python Program to print list the files in a directory.")
Direc = input(r"Enter the path of the folder: ")
print(f"Files in the directory: {Direc}")
files = os.listdir(Direc)
# Filtering only the files.
files = [f for f in files if os.path.isfile(Direc+'/'+f)]
print(*files, sep="\n")

# import OS
import os
for x in os.listdir():
    if x.endswith(".txt"):
        # Prints only text file present in My Folder
        print(x)
        
# import OS module
import os

# This is my path
path = "C://Users//Vanshi//Desktop//gfg"

# to store files in a list
list = []

# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
            print(f)

# import OS module
import os

# This is my path
path = "C://Users//Vanshi//Desktop//gfg"

# Scan the directory and get
# an iterator of os.DirEntry objects
# corresponding to entries in it
# using os.scandir() method
obj = os.scandir(path)

# List all files and directories in the specified path
print("Files and Directories in '% s':" % path)
for entry in obj:
    if entry.is_dir() or entry.is_file():
        print(entry.name)
        
import glob

# This is my path
path = "C:\\Users\\Vanshi\\Desktop\\gfg"

# Using '*' pattern
print('\nNamed with wildcard *:')
for files in glob.glob(path + '*'):
    print(files)

# Using '?' pattern
print('\nNamed with wildcard ?:')
for files in glob.glob(path + '?.txt'):
    print(files)


# Using [0-9] pattern
print('\nNamed with wildcard ranges:')
for files in glob.glob(path + '/*[0-9].*'):
    print(files)
    

import glob

# This is my path
path = "C:\\Users\\Vanshi\\Desktop\\gfg**\\*.txt"


# It returns an iterator which will
# be printed simultaneously.
print("\nUsing glob.iglob()")

# Prints all types of txt files present in a Path
for file in glob.iglob(path, recursive=True):
    print(file)
