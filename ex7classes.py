

class Dir:

    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.subdirs = []
        self.filesize = 0

    def add_subdir(self, dir):
        self.subdirs.append(dir.name)


class Tree:
    def __init__(self):
        self.dirs = []

    def add_dir(self, new_dir: Dir):
        self.dirs.append(new_dir)


readfile()
