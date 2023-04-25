a1 = int(input('enter the first element a1: '))
d = int(input('enter numbers difference d: '))
n = int(input('enter numbers amount n: '))

def arifProg(a, b, c):
    list_1 = list()
    for i in range(1, n + 1):
        list_1.append(a1 + (i - 1) * d)
    return list_1

def printList(list):
    for i in range(len(list)):
        print(list[i])

printList(arifProg(a1, d, n))