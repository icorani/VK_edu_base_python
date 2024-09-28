from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    dq = deque(nums)
    dq.rotate(n)
    return list(dq)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
