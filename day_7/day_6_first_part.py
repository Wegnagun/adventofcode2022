def load_data(file: str) -> str:  # Достаем вводные данные.
    with open(file) as file:
        return file.read()


def main() -> int:
    pass


if __name__ == '__main__':
    result = main()
    print(f'Надо обработать {result} символов а надо 3263')
