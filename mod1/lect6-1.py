#in_str = input().split()
#in_str = 'hello world'.split()
#print(lambda in_str=input().split(): sum(list(len(word) for word in in_str))/len(in_str))
in_str = input().split()
print(round(sum(map(len, in_str)) / len(in_str), 2))
