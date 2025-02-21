
def pascals_triangle(number):
    myList = []
    myList.append([1])
    for i in range(1, number + 1):
        aList = get_list(i)
        myList.append(aList)
    return myList

def get_list(times):
    number = 1
    temp = 0
    myList = []
    for i in range(0, times):
        result = number + temp
        temp = result
        myList.append(result)
        if i == times - 1:
            myList.append(1)
    return myList


print(pascals_triangle(5))