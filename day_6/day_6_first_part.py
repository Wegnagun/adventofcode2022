def load_data(file):  # Достаем вводные данные.
    with open(file) as file:
        return file.read()


def main():
    start_index_packet = 0
    packet = ''
    message = load_data('data.txt')
    for index in range(len(message)):
        if message[index] in packet:
            packet = "" + message[index]
            start_index_packet = index + 1
        else:
            start_index_packet = index + 1
            packet += message[index]
        if len(packet) == 4:
            break
    return start_index_packet


if __name__ == '__main__':
    result = main()
    print(f'Пакет начинается с символа под номером: {result}')
