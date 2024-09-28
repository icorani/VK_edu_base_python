import timeit


def cache_deco(func):
    cache = {'1': 1, '2': 1}

    def wrapper(*args, **kwargs):
        if cache.get(args[0]):
            pass
        else:
            cache[args[0]] = func(*args, **kwargs)
        return cache[args[0]]

    return wrapper


@cache_deco
def fib(k=30):
    if k <= 2:
        return 1
    return fib(k - 1) + fib(k - 2)


def test():
    print('test')


if __name__ == "__main__":
    s = '''
print('started')
fib(600)
    '''
    print(timeit.timeit(stmt=s, setup="from __main__ import fib, cache_deco", number=5))
