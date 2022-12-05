def get_range_list(data):
    range_list = [
        [
            list(map(int, num.split('-'))) for num in pairs.split(',')
        ]
        for pairs in data      # еба, закрутил =D
    ]
    return range_list


def load_data(file):  # Достаем вводные данные.
    with open(file) as file:
        input_data = file.read().split()
    return input_data


def main():
    count = 0
    data = load_data('ttt.txt')
    range_list = get_range_list(data)
    print(range_list)
    for index in range(1, len(range_list)):
        for i in range_list[index]:
            print(i)
    #         if (
    #             range_list[index - 1][0] <= left >= range_list[index][-1]
    #             and range_list[index - 1][0] <= right >= range_list[index][-1]
    #         ):
    #             count += 1
    # print(count)


if __name__ == '__main__':
    main()

# print(f'сумма приоритетов такова: {result}')
