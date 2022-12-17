from typing import Type


class Directory:
    def __init__(self, name: str, parent: Type['Directory'] | None = None):
        self.name = name
        self.parent = parent
        self.children: list[Type['Directory'] | Type["File"]] = []

    def add_child(self, child: Type['Directory'] | Type["File"]):
        self.children.append(child)

    def get_path(self) -> str:
        if self.parent is None:
            return self.name
        parent = self.parent.get_path()
        if parent != '/':
            return f'/{self.name}'

    def get_child(self, name: str) -> Type["Directory"] | Type["File"]:
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError(f'Child {name} не найден')

    def total_size(self, size_cache: dict[str, int] | None = None) -> int:
        curr_path = self.get_path()
        total_size = sum(
            child.total_size(size_cache) if isinstance(child, Directory)
            else child.size for child in self.children
        )
        if size_cache is not None:
            size_cache[curr_path] = total_size
        return total_size

    def __repr__(self):
        return f'{self.name} (dir)'


class File:
    def __init__(self, name: str, parent: Type["Directory"], size: int):
        self.name = name
        self.parent = parent
        self.size = size

    def get_path(self) -> str:
        return f"{self.parent.get_path()}/{self.name}"

    def __repr__(self):
        return f"{self.name} (file, size={self.size})"


def calculate_directory_size(
    root: Directory, size_cache: dict[str, int] | None = None
) -> dict[str, int]:
    if size_cache is None:
        size_cache = {}
    if root.get_path() in size_cache:
        return size_cache
    root.total_size(size_cache)
    return size_cache


def load_data(file: str) -> Directory:  # Достаем вводные данные.
    with open(file) as file:
        lines = file.read().strip().split("\n")
    root: Type[Directory] = Directory("/")
    current_directory = root
    for line in lines:
        match line.split():
            case ["$", "ls"]:
                continue
            case ["$", "cd", ".."]:
                current_directory = current_directory.parent
            case ["$", "cd", "/"]:
                current_directory = root
            case ["$", "cd", directory] if directory != "/":
                current_directory = current_directory.get_child(directory)
            case ["dir", directory]:
                current_directory.add_child(Directory(directory, current_directory))
            case [size, filename]:
                current_directory.add_child(
                    File(filename, current_directory, int(size))
                )
    return root


def main():
    root = load_data('ttt.txt')
    dir_sizes = calculate_directory_size(root)
    return sum([size for size in dir_sizes.values() if size < 100000])


if __name__ == '__main__':
    result = main()
    print(f'Сумма дирректорий: {result}')
