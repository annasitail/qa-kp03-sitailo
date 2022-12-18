from flask import Flask, jsonify, url_for, request, render_template, Response
app = Flask(__name__)


class Directory:

    def __init__(self):
        self.parent = None
        self.name = "root"
        self.MAX_DIR_SIZE = 10
        self.children = []

    @staticmethod
    def create(parent, name, max_size):
        dir = Directory()
        dir.name = name
        dir.MAX_DIR_SIZE = max_size
        if parent == None:
            parent = directory
        if len(parent.children) >= parent.MAX_DIR_SIZE:
            return parent.name + " is full!"
        dir.parent = parent
        dir.parent.children.append(dir)
        return dir

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

    def find(self, path):
        dirs = path.split('/')
        dirs.remove('root')
        result = self
        for name in dirs:
            notFound = True
            for j in result.children:
                if j.name == name and isinstance(j, Directory):
                    result = j
                    notFound = False
                    break
            if notFound:
                return None    
        print(result.name)
        return result

    def find_file(self, name):
        for j in self.children:
            if j.name == name and isinstance(j, File):
                return j
        return None
    
    def delete(self):
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


    @staticmethod
    def create(parent, name, content):
        bin_f = BinaryFile()
        bin_f.name = name
        bin_f.content = content
        if parent == "":
            parent = directory
        if len(parent.children) >= parent.MAX_DIR_SIZE:
            return parent.name + " is full!"
        bin_f.parent = parent
        bin_f.parent.children.append(bin_f)
        return bin_f

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

    def delete(self):
        self.parent.children.remove(self)
        print(self.name + " was deleted successfully!")


class LogTextFile(File):

    def __init__(self):
        File.__init__(self)
        self.parent = None
        self.name = "file"
        self.content = []

    @staticmethod
    def create(parent, name, content):
        log_f = LogTextFile()
        log_f.name = name
        log_f.content.append(content)
        if parent == "":
            parent = directory
        if len(parent.children) >= parent.MAX_DIR_SIZE:
            return parent.name + " is full!"
        log_f.parent = parent
        log_f.parent.children.append(log_f)
        return log_f

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
        result = ""
        for i in self.content:
            result += i + "\n"
        return result

    def append_line(self, line):
        self.content.append(line)
        print("Line was added successfully!")

    def delete(self):
        self.parent.children.remove(self)
        print(self.name + " was deleted successfully!")


class BufferFile(File):

    def __init__(self):
        File.__init__(self)
        self.parent = None
        self.name = "file"
        self.MAX_BUF_FILE_SIZE = 10
        self.content = []

    @staticmethod
    def create(parent, name, max_size):
        buf_f = BufferFile()
        buf_f.name = name
        buf_f.MAX_BUF_FILE_SIZE = max_size
        if parent == "":
            parent = directory
        if len(parent.children) >= parent.MAX_DIR_SIZE:
            print(parent.name + " is full!")
            return
        buf_f.parent = parent
        buf_f.parent.children.append(buf_f)
        return buf_f

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

    def delete(self):
        self.parent.children.remove(self)
        print(self.name + " was deleted successfully!")



def display_structure(element):
    structure = "[" + element.name
    for e in element.children:
        if type(e) is Directory:
            structure += " - dir: " + display_structure(e)
        else:
            structure += " - file: " + e.name
    structure += "]"
    return structure



@app.route('/directory', methods=['GET'])
def display():
    res = request.args.get('name')
    if res != None:
        dir = directory.find(res)
        if dir != None:
            return display_structure(dir)
        else:
            return "Not found", 404
    return display_structure(directory)

@app.route('/directory', methods=['POST'])
def create_dir():
    name = request.json['name']
    max_size = request.json['max_size']
    parent = directory.find(request.json['parent'])
    if parent == None:
        return "Parent directory not found", 404
    dir = Directory.create(parent, name, max_size)
    return "Added successfully " + dir.name + " in " + dir.parent.name
    
@app.route('/directory', methods=['PUT', 'PATCH'])
def move_dir():
    dir = directory.find(request.json['path'])
    if dir == None:
        return "Parent directory not found", 404
    new_parent = directory.find(request.json['new_parent'])
    if new_parent == None:
        return "Parent directory not found", 404
    dir.move(new_parent)
    return "Moved successfully into " + dir.parent.name

@app.route('/directory', methods=['DELETE'])
def delete_dir():
    dir = directory.find(request.json['path'])
    if dir == None:
        return "Not found", 404
    dir.delete()
    return "Deleted"



@app.route('/binaryfile', methods=['POST'])
def create_bin_file():
    name = request.json['name']
    content = request.json['content']
    parent = directory.find(request.json['parent'])
    if parent == None:
        return "Not found", 404
    bin_f = BinaryFile.create(parent, name, content)
    return "Added successfully " + bin_f.name + " in " + bin_f.parent.name
    
@app.route('/binaryfile', methods=['PUT', 'PATCH'])
def move_bin_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    print("Found binary file " + file.name)
    new_parent = directory.find(request.json['new_parent'])
    file.move(new_parent)
    return "Moved successfully into " + file.parent.name

@app.route('/binaryfile', methods=['GET'])
def read_bin_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    return file.read_file()

@app.route('/binaryfile', methods=['DELETE'])
def delete_bin_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    file.delete()
    return "Deleted"



@app.route('/logtextfile', methods=['POST'])
def create_log_file():
    print(directory.name)
    name = request.json['name']
    content = request.json['content']
    parent = directory.find(request.json['parent'])
    log_f = LogTextFile.create(parent, name, content)
    return "Added successfully " + log_f.name + " in " + log_f.parent.name
    
@app.route('/logtextfile', methods=['PUT', 'PATCH'])
def move_log_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    print("Found log text file " + file.name)
    new_parent = directory.find(request.json['new_parent'])
    file.move(new_parent)
    return "Moved successfully into " + file.parent.name

@app.route('/logtextfile', methods=['GET'])
def read_log_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    return file.read_file()

@app.route('/logtextfile', methods=['PUT', 'PATCH'])
def append_log_file():
    line = request.json['line']
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    file.append_line(line)
    return "Line was added successfully"

@app.route('/logtextfile', methods=['DELETE'])
def delete_log_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    file.delete()
    return "Deleted"



@app.route('/bufferfile', methods=['POST'])
def create_buf_file():
    print(directory.name)
    name = request.json['name']
    max_size = request.json['max_size']
    parent = directory.find(request.json['parent'])
    buf_f = BufferFile.create(parent, name, max_size)
    return "Added successfully " + buf_f.name + " in " + buf_f.parent.name
    
@app.route('/bufferfile', methods=['PUT', 'PATCH'])
def move_buf_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    print("Found buffer file " + file.name)
    new_parent = directory.find(request.json['new_parent'])
    file.move(new_parent)
    return "Moved successfully into " + file.parent.name

@app.route('/bufferfile', methods=['PUT'])
def push_buf_file():
    element = request.json['element']
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    file.push(element)
    return "Pushed successfully"

@app.route('/bufferfile', methods=['PUT'])
def consume_buf_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    file.consume()
    return "Consumed successfully"

@app.route('/bufferfile', methods=['DELETE'])
def delete_buf_file():
    path = request.json['path'].split('/')
    file_name = path[len(path)-1]
    dir = directory.find(request.json['path'].replace("/" + file_name, ""))
    if dir == None:
        return "Not found", 404
    file = dir.find_file(file_name)
    file.delete
    return "Deleted"



directory = Directory()

if __name__ == '__main__':
    app.run(debug=True)
