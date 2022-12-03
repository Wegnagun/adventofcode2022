win_data = {'X': 1, 'Y': 2, 'Z': 3}
data_dict = {
    "win": {
        "A": win_data['Y'], "B": win_data['Z'], "C": win_data['X'],
    },
    "lose": {
        "A": win_data['Z'], "B": win_data['X'], "C": win_data['Y'],
    },
    "draw": {
        "A": win_data['X'], "B": win_data['Y'], "C": win_data['Z'],
    }
}
# A = камень : X = камень
# B = бумага : Y = бумага
# C = ножницы : Z = ножницы
# X = проиграть
# Y = ничья
# Z = выиграть


with open('data.txt') as file:
    input_data = file.read().split()
data = [
    input_data[i] + input_data[i + 1] for i in range(0, len(input_data), 2)
]
result = 0
for item in data:
    if item[-1] == 'Z':
        result += data_dict["win"][item[0]] + 6
    elif item[-1] == 'Y':
        result += data_dict["draw"][item[0]] + 3
    elif item[-1] == 'X':
        result += data_dict["lose"][item[0]]


print(data)
print(result)
