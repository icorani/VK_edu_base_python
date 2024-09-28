from typing import List, Dict


def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    res = sorted(d.items(), key=lambda x: x[1], reverse=True)
    result = list()
    for el in res:
        result.append(el[0])
    return result


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
