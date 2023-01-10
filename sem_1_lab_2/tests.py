from main import Directory
from main import BinaryFile
from main import LogTextFile
from main import BufferFile



def test_directory_create():
    directory = Directory()
    directory.create(None, "d1", 15)
    assert directory.parent == None
    assert directory.name == "d1"
    assert directory.MAX_DIR_SIZE == 15

def test_directory_move():
    directory = Directory()
    directory.create(None, "d1", 15)
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    directory.move(parent_directory)
    assert directory.parent == parent_directory

def test_directory_delete():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    directory = Directory()
    directory.create(parent_directory, "d1", 15)
    del directory
    assert 'directory' not in locals()

def test_buffer_file_create():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    buffer_file = BufferFile()
    buffer_file.create(parent_directory, "buffer_file", 15)
    assert buffer_file.name == "buffer_file"
    assert buffer_file.parent == parent_directory
    assert buffer_file.MAX_BUF_FILE_SIZE == 15

def test_buffer_file_move():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    buffer_file = BufferFile()
    buffer_file.create(parent_directory, "buffer_file", 15)
    new_parent_directory = Directory()
    new_parent_directory.create(None, "new", 20)
    buffer_file.move(new_parent_directory)
    assert buffer_file.parent.name == new_parent_directory.name

def test_buffer_file_push_and_consume():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    buffer_file = BufferFile()
    buffer_file.create(parent_directory, "buffer_file", 15)
    buffer_file.push("element to push")
    assert len(buffer_file.content) == 1
    length = len(buffer_file.content)
    buffer_file.consume()
    assert length - len(buffer_file.content) == 1

def test_buffer_file_delete():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    buffer_file = BufferFile()
    buffer_file.create(parent_directory, "buffer_file", 15)
    del buffer_file
    assert 'buffer_file' not in locals()

def test_log_text_file_create():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    log_text_file = LogTextFile()
    log_text_file.create(parent_directory, "log_text_file", "content")
    assert log_text_file.name == "log_text_file"
    assert log_text_file.parent == parent_directory
    assert log_text_file.content == ["content"]

def test_log_text_file_move():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    log_text_file = LogTextFile()
    log_text_file.create(parent_directory, "log_text_file", "content")
    new_parent_directory = Directory()
    new_parent_directory.create(None, "new", 20)
    log_text_file.move(new_parent_directory)
    assert log_text_file.parent.name == new_parent_directory.name

def test_log_text_file_append_and_read():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    log_text_file = LogTextFile()
    log_text_file.create(parent_directory, "log_text_file", "content")
    assert log_text_file.read_file() == log_text_file.content
    log_text_file.append_line("something to add")
    assert log_text_file.content == ["content", "something to add"]

def test_log_text_file_delete():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    log_text_file = LogTextFile()
    log_text_file.create(parent_directory, "log_text_file", "content")
    del log_text_file
    assert 'log_text_file' not in locals()

def test_binary_file_create():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    binary_file = BinaryFile()
    binary_file.create(parent_directory, "binary_file", "content")
    assert binary_file.name == "binary_file"
    assert binary_file.parent == parent_directory
    assert binary_file.content == "content"

def test_binary_file_move():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    binary_file = BinaryFile()
    binary_file.create(parent_directory, "binary_file", "content")
    new_parent_directory = Directory()
    new_parent_directory.create(None, "new", 20)
    binary_file.move(new_parent_directory)
    assert binary_file.parent.name == new_parent_directory.name

def test_binary_file_append_and_read():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    binary_file = BinaryFile()
    binary_file.create(parent_directory, "binary_file", "content")
    assert binary_file.read_file() == "content"

def test_binary_file_delete():
    parent_directory = Directory()
    parent_directory.create(None, "parent_directory", 25)
    binary_file = BinaryFile()
    binary_file.create(parent_directory, "binary_file", "content")
    del binary_file
    assert 'binary_file' not in locals()
