__author__ = "ayengec"
__email__ =  "alicaneem@gmail.com"
""" 
This example shows that lists whatever files with extension in your desired location.

"""

import os

if __name__ == "__main__":
    for path, pathName, folderName in os.walk("C:/Program Files/Notepad++"): # You can change this location
        for filename in folderName:
            if(filename.endswith(".dll")):             # You can change this extension
                with open("dll_files.txt", "a") as textLog:    # All files will be listed in this text file. You can change it.
                    textLog.write(filename)
                    textLog.write("\n")