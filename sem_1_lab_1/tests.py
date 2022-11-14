from main import FileSystem
from main import File
from main import Directory
from main import BinaryFile
from main import LogTextFile
from main import BufferFile
import pytest

class Tests:

    def test_directory_create():
        directory = Directory("", "d1", 15)
        assert directory.parent == ""
        assert directory.name == "d1"
        assert directory.MAX_SIZE == 15

    def test_directory_move():
        directory = Directory("", "d1", 15)
        parent_directory = Directory("", "parent_directory", 25)
        directory.move(parent_directory)
        assert directory.parent == parent_directory

    def test_directory_delete():
        parent_directory = Directory("", "parent_directory", 25)
        directory = Directory(parent_directory, "d1", 15)
        length = parent_directory.len()
        del directory
        assert length - parent_directory.len == 1
        assert 'directory' not in locals()

    def test_buffer_file_create():
        parent_directory = Directory("", "parent_directory", 25)
        buffer_file = BufferFile(parent_directory, "buffer_file", 15)
        assert buffer_file.name == "buffer_file"
        assert buffer_file.parent == parent_directory
        assert buffer_file.MAX_BUF_FILE_SIZE == 15

    def test_buffer_file_move():
        parent_directory = Directory("", "parent_directory", 25)
        buffer_file = BufferFile(parent_directory, "buffer_file", 15)
        new_parent_directory = Directory("", "new", 20)
        assert buffer_file.parent == new_parent_directory

    def test_buffer_file_push():
        parent_directory = Directory("", "parent_directory", 25)
        buffer_file = BufferFile(parent_directory, "buffer_file", 15)
        with pytest.raises(OverflowError):
            for _ in range(16):
                buffer_file.push("element to push")

    def test_buffer_file_consume():
        parent_directory = Directory("", "parent_directory", 25)
        buffer_file = BufferFile(parent_directory, "buffer_file", 15)
        length = buffer_file.len()
        buffer_file.consume("element to consume")
        assert length - buffer_file.len() == 1

    def test_buffer_file_delete():
        parent_directory = Directory("", "parent_directory", 25)
        buffer_file = BufferFile(parent_directory, "buffer_file", 15)
        del buffer_file
        assert 'buffer_file' not in locals()

    def test_log_text_file_create():
        parent_directory = Directory("", "parent_directory", 25)
        log_text_file = LogTextFile(parent_directory, "log_text_file", "content")
        assert log_text_file.name == "log_text_file"
        assert log_text_file.parent == parent_directory
        assert log_text_file.content == "content"

    def test_log_text_file_move():
        parent_directory = Directory("", "parent_directory", 25)
        log_text_file = LogTextFile(parent_directory, "log_text_file", "content")
        new_parent_directory = Directory("", "new", 20)
        assert log_text_file.parent == new_parent_directory

    def test_log_text_file_append_and_read():
        parent_directory = Directory("", "parent_directory", 25)
        log_text_file = LogTextFile(parent_directory, "log_text_file", "content")
        assert log_text_file.read_file() == "content"
        log_text_file.append_line("something to add")
        assert log_text_file.read_file() == "content\nsomething to add"

    def test_log_text_file_delete():
        parent_directory = Directory("", "parent_directory", 25)
        log_text_file = LogTextFile(parent_directory, "log_text_file", "content")
        del log_text_file
        assert 'log_text_file' not in locals()

    def test_binary_file_create():
        parent_directory = Directory("", "parent_directory", 25)
        binary_file = BinaryFile(parent_directory, "binary_file", "content")
        assert binary_file.name == "binary_file"
        assert binary_file.parent == parent_directory
        assert binary_file.content == "content"

    def test_binary_file_move():
        parent_directory = Directory("", "parent_directory", 25)
        binary_file = BinaryFile(parent_directory, "binary_file", "content")
        new_parent_directory = Directory("", "new", 20)
        assert binary_file.parent == new_parent_directory

    def test_binary_file_append_and_read():
        parent_directory = Directory("", "parent_directory", 25)
        binary_file = BinaryFile(parent_directory, "binary_file", "content")
        assert binary_file.read_file() == "content"

    def test_binary_file_delete():
        parent_directory = Directory("", "parent_directory", 25)
        binary_file = BinaryFile(parent_directory, "binary_file", "content")
        del binary_file
        assert 'binary_file' not in locals()
