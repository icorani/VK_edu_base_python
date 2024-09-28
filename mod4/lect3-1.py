import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    return tuple(map(int, datetime.datetime.strftime(datetime.timedelta(days=days, seconds=seconds)
                                                     + datetime.datetime.fromisoformat('2023-01-01 12:30:00'),
                                                     '%d %S').split()))


print(shift_time(days, seconds))
