#numerator, denominator = int(input()), int(input())
numerator, denominator = list(map(int, input().split(',')))


def changed_div(_numerator: int, _denominator: int):
    """

    :type _denominator: int
    :type _numerator: int
    """
    try:
        return _numerator / _denominator
    except ZeroDivisionError:
        return _numerator


print(changed_div(numerator, denominator))
