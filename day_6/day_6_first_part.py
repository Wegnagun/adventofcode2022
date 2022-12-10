def load_data(file):  # Достаем вводные данные.
    with open(file) as file:
        return file.read()


def main() -> int:
    message = load_data('data.txt')
    for index in range(len(message)):
        if (
            len(message[index: index + 4])
            == len(set(message[index: index + 4]))
        ):
            return index + 4


if __name__ == '__main__':
    result = main()
    print(f'Пакет начинается с символа под номером: {result}')
