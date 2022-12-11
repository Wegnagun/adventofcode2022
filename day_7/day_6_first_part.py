class Commands:
    def __init__(self):
        self.current_dir = ['Wegnagun/']
        self.system = {'Wegnagun/': {}}

    def cd(self, dir_name):
        self.current_dir.append(dir_name)
        print(
            f'Перемещаемся из дирректории "{self.current_dir[-2]}" '
            f'в дирректорию "{dir_name}"'
        )
        self.system[self.current_dir[-2]] = {self.current_dir[-1]: []}
        print(self.system)

    def cd_up(self):
        print(
            f'Перемещаемся из дирректории "{self.current_dir[-1]}" '
            f'назад дирректорию "{self.current_dir[-2]}"'
        )
        self.current_dir.pop()

    def ls(self, command):
        print(f'Внутри {command}')
        for i in command:
            if i == 'dir':
                self.system['Wegnagun/'] = {self.current_dir[-1]: []}

    def show(self):
        return self.system


def load_data(file: str) -> list:  # Достаем вводные данные.
    with open(file) as file:
        lines = [line.rstrip().split() for line in file]
        return lines


def main():
    dir = Commands()
    current_dir = None
    print(load_data('ttt.txt'))
    commands = load_data('ttt.txt')
    print('=' * 100)
    for command in commands:
        if command[0] == '$':
            print(f'комманда: {command}')
            if command[1] == 'cd':
                if command[2] == '..':
                    dir.cd_up()
                    continue
                dir.cd(command[2])
                continue
        else:
            dir.ls(command)
            continue
        # print(command)
    print('=' * 100)
    print(dir.show())


if __name__ == '__main__':
    result = main()
    # print(f'Надо обработать {result} символов а надо 3263')
