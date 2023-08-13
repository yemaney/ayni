from ayni.parse import get_python_functions


def test_get_python_functions(test_directory):
    functions = get_python_functions(f"{test_directory}/file2.py")

    assert len(list(functions)) == 3
    for function in functions:
        assert function == "def func1():\n\tpass"
        assert function == "def func2():\n\tpass"
        assert function == "def func3():\n\tpass"
