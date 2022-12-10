# да емана, обрабатываем ввод... плюнул создал матрицу для контейнеров... потом еще плюнул и сделал дек
# containers = [['Z', 'N'], ['M', 'C', 'D'], ['P']]  # тестовые данные
containers = [
    ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],  # 1
    ['D', 'Q', 'L'],                           # 2
    ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],  # 3
    ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],       # 4
    ['V', 'G', 'L', 'F', 'Z', 'S'],            # 5
    ['D', 'G', 'N', 'P'],                      # 6
    ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],       # 7
    ['C', 'P', 'D', 'M', 'S'],                 # 8
    ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C'],  # 9
]


def load_data(file):  # Достаем вводные данные.
    with open(file) as file:
        input_data = [line.rstrip() for line in file]
        moves = [i.split() for i in input_data[10:]]
    return moves


def main():
    final_containers = containers
    moves = load_data('data.txt')
    for actions in moves:
        for move in range(int(actions[1])):
            index_from = int(actions[3]) - 1
            index_to = int(actions[-1]) - 1
            mv = final_containers[index_from].pop()
            final_containers[index_to].append(mv)
    last_containers = ''.join([i[-1] for i in final_containers])
    return last_containers


if __name__ == '__main__':
    result = main()
    print(f'Список верхних(-1) элементов каждого стобца: {result}')
