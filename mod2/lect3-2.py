def filter(func, seq):
    for el in seq:
        if func(el):
            yield el


func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
    print(x)
