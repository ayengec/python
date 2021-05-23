__author__ = "ayengec"
__email__ =  "alicaneem@gmail.com"
""" 
This module explains dictionaries data type in Python.
"""

if __name__ == "__main__":
    myDict = {
        "lang"    : "SV",
        "year"    : 2020,
        "FPGA"    : "Artix-7",
        "isvalid" : True,
        "method"  : "UVM",
    }
    print(myDict)
    # Console Output: {'lang': 'SV', 'year': 2020, 'FPGA': 'Artix-7', 'isvalid': True, 'method': 'UVM'}
    
    print(myDict["year"])
    # Console Output: 2020
    
    print(myDict.keys())
    # Console Output: dict_keys(['lang', 'year', 'FPGA', 'isvalid', 'method'])
    
    print(myDict.values())
    # Console Output: dict_values(['SV', 2020, 'Artix-7', True, 'UVM'])
    
    myDict["FPGA"] = "Zynq-7000 SoC"
    print(myDict)
    # Console Output: {'lang': 'SV', 'year': 2020, 'FPGA': 'Zynq-7000 SoC', 'isvalid': True, 'method': 'UVM'}
    
    del myDict["method"] # Be care! It's different from lists and tuples
    print(myDict)
    # Console Output: {'lang': 'SV', 'year': 2020, 'FPGA': 'Zynq-7000 SoC', 'isvalid': True}
    
    myDict["Clock Freq"] = 10e7 # to add new key and its value to our dict
    print(myDict)
    # Console Output: {'lang': 'SV', 'year': 2020, 'FPGA': 'Zynq-7000 SoC', 'isvalid': True, 'Clock Freq': 100000000.0}
