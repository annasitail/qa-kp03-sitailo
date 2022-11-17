class Directory:

    def __init__(self):
        self.parent = None
        self.name = "root"
        self.MAX_DIR_SIZE = 10
        self.children = []

    def create(self, parent, name, max_size):
        self.name = name
        self.MAX_DIR_SIZE = max_size
        if parent != None:
            if len(parent.children) >= parent.MAX_DIR_SIZE:
                print(parent.name + " is full!")
                return
            self.parent = parent
            self.parent.children.append(self)
            print(self.name + " was created successfully!")
            return

    def move(self, new_parent):
        if new_parent != None:
            if len(new_parent.children) >= new_parent.MAX_DIR_SIZE:
                print(new_parent.name + " is full! Cannot move " + self.name)
                return
            if self.parent != None:
                self.parent.children.remove(self)
            self.parent = new_parent
            self.parent.children.append(self)
            print(self.name + " was moved to " + self.parent.name + " successfully!")
            return
        print(new_parent + " is empty!")
    
    def __delete__(self):
        self.parent.children.remove(self)
        print(self.name + " was deleted successfully!")


class File:

    def __init__(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def move(self):
        pass


class BinaryFile(File):

    def __init__(self):
        File.__init__(self)
        self.parent = None
        self.name = "file"
        self.content = ""

    def create(self, parent, name, content):
        if len(parent.children) >= parent.MAX_DIR_SIZE:
            print(parent.name + " is full!")
            return
        self.parent = parent
        self.name = name
        self.content = content
        self.parent.children.append(self)
        print(self.name + " was created successfully!") 

    def __delete__(self):
        self.parent.children.remove(self)
        print(self.name + " was deleted successfully!")

    def move(self, new_parent):
        if new_parent != None:
            if len(new_parent.children) >= new_parent.MAX_DIR_SIZE:
                print(new_parent.name + " is full! Cannot move " + self.name)
                return
            if self.parent != None:
                self.parent.children.remove(self)
            self.parent = new_parent
            self.parent.children.append(self)
            print(self.name + " was moved to " + self.parent.name + " successfully!")
            return
        print(new_parent + " is empty!")

    def read_file(self):
        print(self.content)
        return self.content


class LogTextFile(File):

    def __init__(self):
        File.__init__(self)
        self.parent = None
        self.name = "file"
        self.content = []

    def create(self, parent, name, content):
        if len(parent.children) >= parent.MAX_DIR_SIZE:
            print(parent.name + " is full!")
            return
        self.parent = parent
        self.name = name
        self.content.append(content)
        self.parent.children.append(self)
        print(self.name + " was created successfully!")

    def __delete__(self):
        self.parent.children.remove(self)
        print(self.name + " was deleted successfully!")

    def move(self, new_parent):
        if new_parent != None:
            if len(new_parent.children) >= new_parent.MAX_DIR_SIZE:
                print(new_parent.name + " is full! Cannot move " + self.name)
                return
            if self.parent != None:
                self.parent.children.remove(self)
            self.parent = new_parent
            self.parent.children.append(self)
            print(self.name + " was moved to " + self.parent.name + " successfully!")
            return
        print(new_parent + " is empty!")

    def read_file(self):
        for i in self.content:
            print(i)
        return self.content

    def append_line(self, line):
        self.content.append(line)
        print("Line was added successfully!")


class BufferFile(File):

    def __init__(self):
        File.__init__(self)
        self.parent = None
        self.name = "file"
        self.MAX_BUF_FILE_SIZE = 10
        self.content = []

    def create(self, parent, name, max_size):
        if len(parent.children) >= parent.MAX_DIR_SIZE:
            print(parent.name + " is full!")
            return
        self.parent = parent
        self.name = name
        self.MAX_BUF_FILE_SIZE = max_size
        self.parent.children.append(self)
        print(self.name + " was created successfully!")

    def __delete__(self):
        self.parent.children.remove(self)
        print(self.name + " was deleted successfully!")

    def move(self, new_parent):
        if new_parent != None:
            if len(new_parent.children) >= new_parent.MAX_DIR_SIZE:
                print(new_parent.name + " is full! Cannot move " + self.name)
                return
            if self.parent != None:
                self.parent.children.remove(self)
            self.parent = new_parent
            self.parent.children.append(self)
            print(self.name + " was moved to " + self.parent.name + " successfully!")
            return
        print(new_parent + " is empty!")

    def push(self, element):
        if len(self.content) >= self.MAX_BUF_FILE_SIZE:
            print("The storage is full!")
            return
        self.content.append(element)

    def consume(self):
        if len(self.content) != 0:
            self.content.pop()
        print("Deleted successfully!")

def display_structure(element):
    structure = "[" + element.name
    # if type(element) is Directory:
    for e in element.children:
        if type(e) is Directory:
            structure += " - dir: " + display_structure(e)
        else:
            structure += " - file: " + e.name
    structure += "]"
    return structure

root_dir = Directory()
root_dir.create(None, "root", 20)
child_dir_1 = Directory()
child_dir_1.create(root_dir, "child_dir_1", 10)
child_dir_2 = Directory()
child_dir_2.create(root_dir, "child_dir_2", 5)

binary_file_1 = BinaryFile()
binary_file_1.create(child_dir_1, "binary_file_1", "This is something in the binary file")
binary_file_2 = BinaryFile()
binary_file_2.create(child_dir_2, "binary_file_2", "One more binary file and its content")

log_text_file_1 = LogTextFile()
log_text_file_1.create(root_dir, "log_text_file_1", "Content of the log text file")
log_text_file_2 = LogTextFile()
log_text_file_2.create(child_dir_2, "log_text_file_2", "Some text in the file")

buffer_file_1 = BufferFile()
buffer_file_1.create(child_dir_1, "buffer_file_1", 3)
buffer_file_2 = BufferFile()
buffer_file_2.create(root_dir, "buffer_file_2", 5)

print("\n" + display_structure(root_dir))
