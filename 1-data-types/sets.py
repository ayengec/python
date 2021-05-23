__author__ = "ayengec"
__email__ =  "alicaneem@gmail.com"
""" 
This module explains sets data type in Python
"""

if __name__ == "__main__":
    mySet1 = {"ayengec", "SV", "Py", "ayengec", "Py"}  # Python automatically removes the duplicates
    print(mySet1)
    # Console Output: {'ayengec', 'SV', 'Py'}
    
    mySet1.add("Computer")
    print(mySet1)
    # Console Output: {'Computer', 'Py', 'SV', 'ayengec'}
    
    mySet1.remove("ayengec")
    print(mySet1)
    # Console Output: {'SV', 'Py', 'Compputer'}
    
    print("SV" in mySet1)       # to evaluate is any string in our set?
    # Console Output: True
    
    ##########################################################################
    
    mySet2 = {"SV", "Py", "C++", "Java"}
    
    mutuals = mySet1 & mySet2   # to find mutual elements
    print(mutuals)
    # Console Output: {'Py', 'SV'}
    
    diffs1_2 = mySet1.difference(mySet2)
    print(diffs1_2)
    # Console Output: {'Computer'}
    
    diffs2_1 = mySet2.difference(mySet1)
    print(diffs2_1)
    # Console Output: {'C++', 'Java'}
    
    print(set(mySet1).issubset(mySet2))
    # Console Output: False
    
    print(set(mySet2).issuperset({"C++","Java"}))
    # Console Output: True
