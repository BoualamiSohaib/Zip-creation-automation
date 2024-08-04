import os
import zipfile

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
    zipName = input("input name for the zip file: ") + ".zip"
     


def main():
    toZip = fileExist()
    createZip(toZip)

main()
