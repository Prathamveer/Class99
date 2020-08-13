import os 
import shutil

source = input("Enter the path of the source folder that has to be backed up: ")
destination = input("Enter the path of the destination folder: ")

list_of_files = os.listdir(source)

for file in list_of_files:
	shutil.copy((source + file), destination)	