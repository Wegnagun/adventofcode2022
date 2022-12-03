with open('data.txt') as file:
    input_data = file.read().replace('\n', ' ')
data = input_data.split('  ')

result = []
for items in data:
    temp = 0
    for item in items.split():
        temp += int(item)
    result.append(temp)
sorted_res = sorted(result)[-1:-4:-1]
print(sum(sorted(result)[-1:-4:-1]))