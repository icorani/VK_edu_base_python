def simple():
    start, end, step = map(int, input().split())
    result = list()
    for el in range(start, end, step):
        if el % 2 == 0:
            result.append(-el)
        else:
            result.append(el*el)
    print(' '.join(str(x) for x in result))

