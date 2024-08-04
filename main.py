import os
import zipfile
import shutil

def fileExist():
    file = input("Please enter the file or Folder path: ")
    
    # Check if the provided input is a valid file or directory path
    if os.path.isfile(file):
        print("The file exists.")
        return file
    elif os.path.isdir(file):
        print("The directory exists.")
        return file
    else:
        print("The path does not exist or the input is incorrect.")
        return None

def createZip(toZip):
    zipName = input("Input name for the zip file: ") + ".zip"


def main():
    toZip = fileExist()
    if toZip:
        zip_file = createZip(toZip)


main()
