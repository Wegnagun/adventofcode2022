# да емана, обрабатываем ввод, плюнул создал матрицу для контейнеров...
containers = [['', 'D', ''], ['N', 'C', ''], ['Z', 'M', 'P'], [1, 2, 3]] # тестовые данные


def load_data(file):  # Достаем вводные данные.
    with open(file) as file:
        input_data = [line.rstrip() for line in file]
        moves = input_data[5:]
    return moves


def main():
    moves = load_data('ttt.txt')
    return moves


if __name__ == '__main__':
    result = main()
    print(result, containers)
    # print(f'Количество входящих в друг друга =) пар: {result}')
