import os
import zipfile
import shutil
from plyer import notification
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
    
    with zipfile.ZipFile(zipName, 'w') as zipf:
        if os.path.isfile(toZip):
            zipf.write(toZip)
        elif os.path.isdir(toZip):
            for root, dirs, files in os.walk(toZip):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), toZip))
    
    notification.notify(
    title="Zip file created",
    message="The zip file have been created successfully go to downloads!",
    app_icon=None,  
    timeout=5  
    )
    return zipName

def moveToDownloads(zip_file):
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    destination = os.path.join(downloads_folder, zip_file)
    shutil.move(zip_file, destination)
    print("Zip file moved to downloads folder.")

def main():
    toZip = fileExist()
    if toZip:
        zip_file = createZip(toZip)
        moveToDownloads(zip_file)

main()
