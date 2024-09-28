from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    d = defaultdict(list)
    for k, v in specializations:
        d[k].append(v)
    return dict(d)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
