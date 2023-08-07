from ayni.codebase_search import find_all_code


def test_find_all_code_python(test_directory):
    for fp in find_all_code(test_directory, [".py"]):
        assert fp.endswith(".py")
