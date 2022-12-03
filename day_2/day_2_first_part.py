data_dict = {
    'CY': 0, 'BX': 0, 'CZ': 3, 'AY': 6,
    'AX': 3, 'BZ': 6, 'CX': 6, 'BY': 3, 'AZ': 0
}
win_data = {'X': 1, 'Y': 2, 'Z': 3}
# A = камень : X = камень
# B = бумага : Y = бумага
# C = ножницы : Z = ножницы


with open('data.txt') as file:
    input_data = file.read().split()
data = [
    input_data[i] + input_data[i + 1] for i in range(0, len(input_data), 2)
]
result = 0
for item in data:
    result += data_dict[item]
    result += win_data[item[1]]

print(data)
print(result)