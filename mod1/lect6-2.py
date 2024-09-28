number_of_records = int(input())
result_list = []
for i in range(number_of_records):
    result_list.append(max(map(int, input().split())))
printed = sorted(result_list, reverse=True)
print(*printed, sep=";")
