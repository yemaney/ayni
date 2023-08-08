from ayni.parse import get_python_functions


def test_get_python_functions(test_directory):
    functions = get_python_functions(f"{test_directory}/file2.py")

    assert len(functions) == 3
    assert functions[0] == "func1"
    assert functions[1] == "func2"
    assert functions[2] == "func3"
