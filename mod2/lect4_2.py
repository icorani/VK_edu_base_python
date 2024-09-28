import functools


def repeat_deco(n=1):
    def outer_func(func):
        def wrapper(*args):
            result = 0
            for i in range(n):
                result = func(*args)
            return result

        return wrapper

    return outer_func


@repeat_deco(3)
def add(seq, val):
    seq.append(val)
    return seq


@repeat_deco(4)
def hello():
    print("hello")


def main():
    code = []
    while data := input():
        code.append(data)
    code = "\n".join(code)
    exec(code)


if __name__ == "__main__":
    hello()
