import string

result = 0
# создаем словари приоритетов
items_priorities = {
    item: number + 1 for number, item in enumerate(string.ascii_letters)
}

# достаем вводные данные
with open('data.txt') as file:
    input_data = file.read().split()

for items in input_data:
    first_compartments = items[:len(items) // 2]
    second_compartments = items[(len(items) // 2):]
    union = set(i for i in first_compartments if i in second_compartments)
    result += items_priorities[list(union)[0]]

print(f'сумма приоритетов такова: {result}')
