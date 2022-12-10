def get_range_list(data):
    range_list = [
        [
            list(map(int, num.split('-'))) for num in pairs.split(',')
        ]
        for pairs in data      # да уж =D
    ]
    return range_list


def load_data(file):  # Достаем вводные данные.
    with open(file) as file:
        input_data = file.read().split()
    return input_data


def main():
    count = 0
    data = load_data('data.txt')
    range_list = get_range_list(data)
    for index in range(0, len(range_list)):
        pair = range_list[index]
        left_range = set(_ for _ in range(pair[0][0], pair[0][1] + 1))
        right_range = set(_ for _ in range(pair[1][0], pair[1][1] + 1))
        if len(left_range & right_range) > 0:
            count += 1
    return count


if __name__ == '__main__':
    result = main()
    print(f'Колличество нахлестывающих пар: {result}')
