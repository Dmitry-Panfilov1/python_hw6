a = int(input('enter numbers amount a: '))
array = list()

def fillArray(list1, n):
    for i in range(n):
        list1.append(int(input('enter array element: ')))
    return list1

minV = int(input('enter min: '))
maxV = int(input('enter max: '))

def arrayDiap(list1, minVal, maxVal):
    listNew = list()
    for i in range(len(list1)):
        if list1[i] >= minVal and list1[i] <= maxVal:
            listNew.append(i+1)
    return listNew

print(*(arrayDiap(fillArray(array, a), minV, maxV)))