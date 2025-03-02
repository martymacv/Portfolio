import os
from zipfile import ZipFile


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.base_folder = None
        self.link = self

    def __setattr__(self, key, value):
        units = ['B', 'KB', 'MB', 'GB']
        if key == 'size':
            count = 0
            while value > 1024:
                count += 1
                value //= 1024
            value = f"{value} {units[count]}"
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def get_base_folder(self):
        return self.base_folder

    def set_base_folder(self, folder):
        self.base_folder = folder


class Folder:
    def __init__(self, name):
        self.name = name
        self.sub_folders_list = list()
        self.file_list = list()
        self.link = self

    def get_folder_name(self):
        return self.name

    def add_file(self, file):
        file.set_base_folder(self)
        self.file_list.append(file)


class Tree:
    def __init__(self, name):
        self.name = name
        self.base_folder = Folder('')

    def find(self, folder_list: list, name: str):
        for folder in folder_list:
            if folder.name == name:
                return folder.link

    def add_new_file(self, path: tuple, file: str, size: int):
        print(path, file, size)
        last_folder = self.base_folder
        if path == ['']:
            last_folder.file_list.append(File(name=file, size=size))
        else:
            for folder_name in path:
                if folder_name not in list(map(Folder.get_folder_name, last_folder.sub_folders_list)):
                    last_folder.sub_folders_list.append(Folder(folder_name))

                last_folder = self.find(last_folder.sub_folders_list, folder_name)
            if file != '':
                # print(file)
                added_file = File(name=file, size=size)
                # added_file.set_base_folder(last_folder)
                last_folder.add_file(file=added_file)

    def print_paths(self):
        for file in self.base_folder.file_list:
            print(f"{file.name} {file.size}")
        for folder in self.base_folder.sub_folders_list:
            if folder.name:
                print(folder.name)
            # print(folder.sub_folders_list)
            i, j = 0, 0
            indent = ''
            sub_folder = folder
        #     print(f"{indent}{sub_folder.name}")
            while sub_folder.sub_folders_list:
                indent += '  '
                for file in sub_folder.file_list:
                    print(f"{indent}{file.name} {file.size}")
                for sub_folder in sub_folder.sub_folders_list:
                    print(f"{indent}{sub_folder.name}")
                for file in sub_folder.file_list:
                    print(f"{indent}  {file.name} {file.size}")
                i += 1




tree = Tree('tree')
with ZipFile('desktop.zip') as zp:
    # print(*zp.infolist(), sep='\n')
    info = zp.infolist()
    for info in zp.infolist():
        file, size = None, None
        path = os.path.split(info.filename)[0].split('/')

        if info.is_dir():
            file = ''
            size = 0
        else:
            file = os.path.split(info.filename)[1]
            size = info.file_size
        # if path[0] != '':
        # print(path, file, size)
        tree.add_new_file(path, file, size)
    # print(create_dir_struct(list(map(lambda x: x.filename, info))))


tree.print_paths()

# def func(base_dict: dict, keys_list: tuple, i: int) -> dict:
#     try:
#         dir_struct[][][][][][][][][][][][].setdefault(keys_list[i], dict())
#         base_dict.setdefault(keys_list[i], dict())
#         return func(base_dict, keys_list, i + 1)
#         # if i:
#         #     return func(base_dict[keys_list[i]], keys_list, i + 1)
#         # else:
#         #     return func(base_dict, keys_list, i + 1)
#     except:
#         return base_dict


# print(func(dict(), ('fun', 'movies'), 0))
