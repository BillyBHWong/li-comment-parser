#os (misc operating system interface): interact with directory
#win32ui: windows ui, message box, etc
import os, win32ui

#list name of all files in a specified directory
files = os.listdir("C:/Users/Billy Wong/Desktop/WAFS")
print(files)

#read a specific file
path = 'days.txt'

#return an array by lines with \n in the end of every line
days_file = open(path, 'r')
lines = days_file.readlines()
print(lines)

#write over a file, create a file if it does not exist
new_day = open('newdays.txt', 'w+')
for i in range(10):
    new_day.write("Number %d\r\n" % (i+1))
print('newdays.txt has been created')

#close file after written
new_day.close()
