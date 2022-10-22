import os
from os import getcwd, listdir
from os.path import isfile, join

cwd = getcwd()
print(getcwd())  # pokazuje obecny folder

for f in listdir(cwd):
    print(f'file={f}, isfile={isfile(join(cwd, f))}')

os.remove('badfile.txt')  # usuwa taki plik

# walk
# [https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory]
