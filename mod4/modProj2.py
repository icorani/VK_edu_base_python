import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n: int) -> List[int]:
    months = [
        datetime.datetime.strptime(date_, "%Y-%m-%dT%H:%M:%S").date().month
        for date_ in dates
    ]
    return [x[0] for x in Counter(months).most_common(n)]


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
