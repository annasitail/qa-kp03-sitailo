from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/resource', methods=['POST', 'GET'])
def resource():
    pass


class Directory:

    @app.route('/directory', methods=['POST', 'GET'])
    def directory():
        pass
    
    @app.route('/directory/create', methods=['POST', 'PUT'])
    def __init__(self, parent, name, max_size):
        pass

    @app.route('/directory/move', methods=['POST', 'PUT', 'PATCH'])
    def move(self, new_parent):
        pass

    @app.route('/directory/delete', methods=['DELETE'])
    def __delete__(self):
        pass


class BinaryFile:

    @app.route('/binaryfile', methods=['POST', 'GET'])
    def binaryfile():
        pass

    @app.route('/binaryfile/create', methods=['POST', 'PUT'])
    def __init__(self, parent, name, content):
        pass

    @app.route('/binaryfile/move', methods=['POST', 'PUT', 'PATCH'])
    def move(self, new_parent):
        pass

    @app.route('/binaryfile/read', methods=['GET'])
    def read_file(self):
        pass

    @app.route('/binaryfile/delete', methods=['DELETE'])
    def __delete__(self):
        pass


class LogTextFile:

    @app.route('/logtextfile', methods=['POST', 'GET'])
    def logtextfile():
        pass

    @app.route('/logtextfile/create', methods=['POST', 'PUT'])
    def __init__(self, parent, name, content):
        pass

    @app.route('/logtextfile/move', methods=['POST', 'PUT', 'PATCH'])
    def move(self, new_parent):
        pass

    @app.route('/logtextfile/read', methods=['GET'])
    def read_file(self):
        pass

    @app.route('/logtextfile/append', methods=['POST', 'PUT', 'PATCH'])
    def append_line(self, line):
        pass

    @app.route('/logtextfile/delete', methods=['DELETE'])
    def __delete__(self):
        pass


class BufferFile:

    @app.route('/bufferfile', methods=['POST', 'GET'])
    def bufferfile():
        pass

    @app.route('/bufferfile/create', methods=['POST', 'PUT'])
    def __init__(self, parent, name, max_size):
        pass

    @app.route('/bufferfile/move', methods=['POST', 'PUT', 'PATCH'])
    def move(self, new_parent):
        pass

    @app.route('/bufferfile/push', methods=['POST', 'PUT', 'PATCH'])
    def push(self, element):
        pass

    @app.route('/bufferfile/consume', methods=['POST', 'PUT', 'PATCH'])
    def consume(self):
        pass

    @app.route('/bufferfile/delete', methods=['DELETE'])
    def __delete__(self):
        pass


if __name__ == '__main__':
    pass
