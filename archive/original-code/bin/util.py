import os
from pathlib import Path
import os, fnmatch


def find(name, path=Path(__file__).root):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def find_dir(name, path= Path(__file__).root):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return os.path.join(root, name)


def find_all(name, path= Path(__file__).root):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def find_pattern(pattern, path= Path(__file__).root):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


if __name__ == '__main__':
    path = find_dir('test_2020')
    file = find_pattern('j1*.in', path)
    print(path)
    print(file)
    # file_object = open(path[0])
    # print(file_object.readlines())
