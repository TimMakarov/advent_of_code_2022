
from ex7classes import *
import sys
sys.path.append("..")

t = ex7classes.Tree()


def readfile():
    F_NAME = 'input7.txt'
    with open(F_NAME, 'r') as file:
        lines = [line.rstrip() for line in file]

    return (lines)


commands = []
god_of_dir = Dir('god', None)
current_dir = Dir('/', god_of_dir)
list_of_dirs = [current_dir]


def process():
    p1 = Dir('name', '/')
    print(p1.name)
    p2 = Dir('name2', p1.name)
    p1.add_subdir(p2)
    print(p2.parent_dir)
    arr = []
    arr.append(p1)
    print(arr[0].parent_dir)


def change_dir(line):
    global current_dir
    if line == '$ cd ..':
        current_dir = current_dir.parent_dir
    else:
        target = line.split(' ')[2]
        print(target)


def list_dir(contents_of_dir):
    pass


def get_next_line():
    global commands
    line = next(commands)
    if line.startswith('$ cd'):
        change_dir(line)
    else:
        print(line)


def main():
    tree = Tree()
    _ROOT = Dir('/', None)
    tree.add_dir(_ROOT)

    commands = iter(readfile())
    # line = next(commands)
    print(next(commands))
    print('before: ', current_dir.name)
    change_dir('$ cd asd')
    print('after', current_dir.name)
    '''
    while True:
        try:
            get_next_line()
        except:
            break
    # process()
'''


if __name__ == '__main__':
    main()
