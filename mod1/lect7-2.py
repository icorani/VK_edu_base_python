from collections import Counter
result = Counter(input().lower().split()).most_common()[0]
print(result[0], result[1])
