def load_data(file):  # Достаем вводные данные.
    with open(file) as file:
        input_data = file.read().split()
    return input_data


def main():
    data = load_data('ttt.txt')
    return data


if __name__ == '__main__':
    result = main()
    print(result)
    # print(f'Количество входящих в друг друга =) пар: {result}')
