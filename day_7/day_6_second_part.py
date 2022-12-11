def load_data(file: str) -> str:  # Достаем вводные данные.
    with open(file) as file:
        return file.read()


def main() -> int:
    message = load_data('data.txt')
    for index in range(len(message)):
        if (
            len(message[index: index + 14])
            == len(set(message[index: index + 14]))
        ):
            return index + 14


if __name__ == '__main__':
    result = main()
    print(f'Надо обработать {result} символов а надо 3263')
