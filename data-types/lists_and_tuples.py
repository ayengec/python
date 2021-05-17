def listsFunc():
    ##################### LISTS ############################
    myList = ["SV", 1905, "python", 10.58, "ayengec"]
    print(str(myList) + " Length of the myList is " + str(len(myList)))
    # Console Output: ['SV', 1905, 'python', 10.58, 'ayengec'] Length of the myList is 5
    
    myList.extend(["new", "list", "appended", True]) # if it was append(), myList would be nested list! Be care while using extend or append
    print(myList)
    # Console Output: ['SV', 1905, 'python', 10.58, 'ayengec', 'new', 'list', 'appended', True]
    
    del(myList[4]) # 4. index "ayengec" will be deleted
    print(myList)
    # Console Output: ['SV', 1905, 'python', 10.58, 'new', 'list', 'appended', True]
    
    squares = list( map(lambda x: x**2, range(6)) )
    print(squares)
    # Console Output: [0, 1, 4, 9, 16, 25]
    
    ### Nested Lists ###
    matrix = [
        [1, 0, 5, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 0, 1, 1]
             ]  # Indeed this definition is nested list: lists in list
    
    print(matrix[0][2]) # 2. index of 0.index of matrix list. So these are rows and columns
    # Console Output: 5
    
    matrix.append([1,2,3,4])
    print(matrix)
    # Console Output: [[1, 0, 5, 1], [1, 1, 0, 1], [1, 0, 1, 1], [0, 0, 1, 1], [1, 2, 3, 4]]
    
    ################### END OF LISTS #######################

def tupleFunc():
    ##################### TUPLES ###########################
    # Note: Tuples are immutable
    tupOne = ("ayengec", 1905, True)
    print(tupOne)
    # Console Output: ('ayengec', 1905, True)
    
    tupTwo = ("SV", 3)
    tupThree = tupOne + tupTwo
    print(str(tupThree) + " length of the tupThree is " + str(len(tupThree)) )
    # Console Output: ('ayengec', 1905, True, 'SV', 3) length of the tupThree is 5
    print(str(tupThree[3]) + " is 3. element of tupThree" )
    # Console Output: SV is 3. element of tupThree
    
    mixedNums = (0, 999, -3, 5, 4, 2, -1, 56, 77)
    sortedNums = sorted(mixedNums) # sorting method of tuples
    print(sortedNums)
    # Console Output: [-3, -1, 0, 2, 4, 5, 56, 77, 999]
    ################### END OF TUPLES ######################
    
if __name__ == "__main__":
    tupleFunc()
    print("########################################################")
    listsFunc()
