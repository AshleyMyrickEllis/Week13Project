#!/usr/bin/env python3.7

#print files in the working directory
import os
cwd = os.getcwd()

#create an empty list
list =[]

# How to check file size within a directory
file_stat = os.stat('Week13Project')
print(file_stat.st_size)

# How to check file size in bytes
file_size = os.path.getsize('/usr/lib64/python3.7/genericpath.py')
print("file size :", file_size, "bytes")


#print list of all files
import os
path = "/home/ec2-user/environment/Week13Project"
dirs = os.listdir(path)

print ("Here is a list of all files")

for filenumber in range(len(dirs)):
    print(filenumber, dirs[filenumber])
    
#List path file and size
for item in os.listdir():
    file_details = os.stat(item)
    list.append({'path':path+'/'+item, 'size':file_details.st_size})
    
print(*list, sep="\n")
    