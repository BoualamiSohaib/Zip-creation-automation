# Zip-Creation-Automation

## Overview

This project is a Python script designed to help users create zip files from a specified file or folder. The script verifies the existence of the provided path, creates a zip file, and moves the zip file to the Downloads folder. Notifications are provided upon successful creation of the zip file.

## Features

- Verify if the given path is a file or directory.
- Create a zip file from the specified file or folder.
- Move the created zip file to the Downloads folder.
- Notify the user upon successful creation of the zip file.

## Libraries Used

- `os`: For interacting with the operating system and handling file paths.
- `zipfile`: For creating and writing zip files.
- `shutil`: For moving the created zip file to the Downloads folder.
- `plyer`: For sending desktop notifications to the user.

## Prerequisites

Ensure you have Python installed. This script is compatible with Python 3.x. Additionally, you need to install the `plyer` library if it's not already installed:

```sh
pip install plyer
```

## Usage

1. Clone the repository or download the script file to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

    ```sh
    python your_script_name.py
    ```

4. Follow the prompts:
   - Enter the file or folder path you wish to zip.
   - Enter a name for the zip file.
5. Upon successful creation, the zip file will be moved to your Downloads folder, and a notification will be displayed.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Your contributions are welcome!
