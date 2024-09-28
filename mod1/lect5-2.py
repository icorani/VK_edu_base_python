result = ''
counter = 0
sym: str
for sym in input():
    if sym in ("!", "%", "#", "@"):
        counter += 1
        result += ''
        continue
    result += sym
print(counter, result.lower(), sep='\n')
