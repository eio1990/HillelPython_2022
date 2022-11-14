A = [10, 10, 23, 10, 123, 66, 78, 123]


def count():
    counter = {}
    for elem in A:
    counter[elem] = counter.get(int(elem), 0 + 1)

    doubles = {element: count for element, count in counter.items() if count > 1}
    return doubles

count()

# print(doubles)