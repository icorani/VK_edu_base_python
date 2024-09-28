def cache_deco(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if cache.get(args[0]):
            pass
        else:
            cache[args[0]] = func(*args, **kwargs)
        return cache[args[0]]

    return wrapper


def solution(func_map, func_filter, data):
    result = filter(func_filter, data)
    result = map(func_map, result)
    return (x for num, x in enumerate(result) if num % 2 == 0)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
