import datetime

string_datetime = input()


def parse_time(s):
    return int(datetime.datetime.strftime(datetime.timedelta(days=1)
                                          + datetime.datetime(*map(int, s.split())), '%d'))


print(parse_time(string_datetime))
