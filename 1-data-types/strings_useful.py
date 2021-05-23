__author__ = "ayengec"
__email__ =  "alicaneem@gmail.com"
""" 
This module explains string methods in Python. If your Python version lower than 3.9, you must comment removesuffix() and removeprefix() method's lines.
"""

if __name__ == "__main__":  # main process of our code. it's important for big projects
    strVar = "ayengec"
    print(strVar)
    # Console Output: 'ayengec'

    print("The length of "+ strVar+ "=" + strVar[::2])
    # Console Output: The every second element= The length of ayengec=aegc

    print("The -2. index is= " + strVar[-2])
    # Console Output: The -2. index is= e

    print("The every second element= " + strVar[::2])
    # Console Output: The every second element= aegc

    print("All chars are uppercase:" + strVar.upper())
    # Console Output: All chars are uppercase:AYENGEC

    print("All chars are lowercase:" + strVar.lower())
    # Console Output: All chars are lowercase:ayengec

    print("Only first char is upper:" + strVar.capitalize())
    # Console Output: Only first char is upper:Ayengec

    print(strVar.find("en")) # returns index number that starts with given char sequence
    # Console Output: 2

    print(strVar.find("xy")) # returns -1 meaning "False" if there is not any char sequence
    # Console Output: -1

    print(strVar.removeprefix('aye')) # new with Python 3.9 version
    # Console Output: Only first char is upper:ngec

    print(strVar.removesuffix('ec')) # new with Python 3.9 version
    # Console Output: Only first char is upper:ayeng
    
    ######################################################## Other Useful Methods ############################################################################
    strSentence = "ayengec user is new in GitHub \nThere are two repos as Systemverilog and Python. \nYou can clone and more repos will be added. Thank you"

    print("split() method:")
    print(strSentence.split('.'))  # it splits whole sequence with given char as '.' and returns as list.
    # Console output:
    # split() method
    # ['ayengec user is new in GitHub \nThere are two repos as Systemverilog and Python', ' \nYou can clone and more repos will be added', ' Thank you']

    print("title() method:")
    print(strSentence.title()) # It capitalizes the first characters of all words, such as titles.
    # Console output:
    # title() method
    # Ayengec User Is New In Github 
    # There Are Two Repos As Systemverilog And Python. 
    # You Can Clone And More Repos Will Be Added. Thank You

    print("splitlines() method:")
    print(strSentence.splitlines())
    # Console output: ['ayengec user is new in GitHub ', 'There are two repos as Systemverilog and Python. ', 'You can clone and more repos will be added. Thank you']
