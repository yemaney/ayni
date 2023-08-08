import os
import tempfile

import pytest


@pytest.fixture
def test_directory():
    # Create a temporary test directory and files for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create and write files inside the temporary directory
        with open(os.path.join(temp_dir, "file1.txt"), "w") as file1:
            file1.write("Test content for file1")

        with open(os.path.join(temp_dir, "file2.py"), "w") as file2:
            file2.write("def func1():\n\tpass\ndef func2():\n\tpass\ndef func3():\n\tpass")

        # Create a subdirectory inside the temporary directory
        subdirectory_path = os.path.join(temp_dir, "subdir")
        os.mkdir(subdirectory_path)

        with open(os.path.join(subdirectory_path, "file3.py"), "w") as file3:
            file3.write('print("This is a Python file")')

        yield temp_dir
