class Directory:

    def __init__(self):
        self.directories = []
        self.files = []

    def create(self, path: str):
        pass

    def delete(self, path: str):
        pass

    def move(self, path: str):
        pass


class File:

    def __init__(self, path):
        self.filepath = path

    def create(self):
        pass

    def delete(self):
        pass

    def move(self):
        pass


class BinaryFile(File):

    def __init__(self, path):
        File.__init__(self, path)

    def create(self):
        pass

    def delete(self):
        pass

    def move(self):
        pass

    def read_file(self):
        return "file content"


class LogTextFile(File):

    def __init__(self, path):
        File.__init__(self, path)

    def create(self):
        pass

    def delete(self):
        pass

    def move(self):
        pass

    def read_file(self):
        return "file content"


class BufferFile(File):

    MAX_BUF_FILE_SIZE = 1024

    def __init__(self, path):
        File.__init__(self, path)

    def create(self):
        pass

    def delete(self):
        pass

    def move(self):
        pass

    def push(self, element: str):
        pass

    def consume(self):
        pass


class FileSystem:

    def init(self):
        self.directories = []
        self.files = []

    def add_directory(self, directory: Directory):
        pass

    def delete_directory(self, path: str):
        pass
    
    def add_file(self, file: File):
        pass

    def delete_file(self, path: str):
        pass

    def get_dir_by_path(self, path: str):
        pass
