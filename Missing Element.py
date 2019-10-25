#Find the missing element between two lists
def finder(arr1, arr2):
    return sum(arr1) - sum(arr2)
#This past solution is a fast and valid one, as long as the elements are all positive.
#So lets find more solutions in case needed for this exemption.

#--------------------------------------------------------------
# Another correct version, but this time with the (zip function)
def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]

#---------------------------------------------------------------
#Soluition with XOR (exclusive OR)
def finder3(arr1, arr2):
    result = 0
    for num in arr1+arr2:
        result^=num

    return result