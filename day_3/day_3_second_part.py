import string

result = 0
# создаем словари приоритетов
items_priorities = {
    item: number + 1 for number, item in enumerate(string.ascii_letters)
}

# достаем вводные данные
with open('data.txt') as file:
    input_data = file.read().split()

data, temp, counter = [], [], 0

for items in input_data:
    temp.append(items)
    counter += 1
    if counter == 3:
        counter = 0
        data.append(temp)
        temp = []

for items in data:
    union = set(i for i in items[0] if i in items[1] and i in items[2])
    result += items_priorities[list(union)[0]]

print(f'сумма приоритетов такова: {result}')
