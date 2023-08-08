"""This module is concerned with code responsible for parsing files for functions.
"""

import os

from tree_sitter import Language, Parser

LANG_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/build/my-languages.so"


def get_python_functions(file_path: str) -> list:
    """
    Loads a python file and parses each function name in the python file.

    Parameters
    ----------
    file_path : str
        file path to a python file

    Returns
    -------
    list
        list of function names found in the file
    """

    with open(file_path) as fp:
        source_code = fp.read()

    # Initialize the Python language
    PYTHON_LANGUAGE = Language(LANG_DIR, "python")
    parser = Parser()
    parser.set_language(PYTHON_LANGUAGE)

    tree = parser.parse(bytes(source_code, "utf-8"))
    root_node = tree.root_node

    functions = []

    # Traverse the AST to find function definitions
    for node in root_node.children:
        if node.type == "function_definition":
            function_name_node = node.child_by_field_name("name")
            function_name = source_code[function_name_node.start_byte : function_name_node.end_byte]
            functions.append(function_name)

    return functions
