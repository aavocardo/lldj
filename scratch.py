list1 = [6, 12, 18, 36]
list2 = [14, 21, 26, 35]
# i want
# list1 = [12, 18, 36, 6]
# list2 = [14, 21, 35, 26]
# main.py output
# list1 = [36, 6, 18, 12]
# list2 = [35, 14, 26, 21]


def sort(a: list, b: list):
    smol: list = []
    for i in range(len(a)):
        for j in range(len(b)):
            smol.append(abs(b[j]-a[i]))
        smol.append('next')
    print(smol)


sort(list1, list2)
