from typing import List


def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    result = list()
    for place, tog in enumerate(zip(nums1, nums2)):
        if tog[0] < tog[1]:
            result.append(place)
    return result


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
