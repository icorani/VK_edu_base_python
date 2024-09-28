a, b = map(int, (input(), input()))
flag = True
while x := input():
    if int(x) < a or int(x) > b:
        flag = False
print(flag)
