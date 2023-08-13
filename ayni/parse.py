"""This module is concerned with code responsible for parsing files for functions.
"""

import os

from tree_sitter import Language, Parser

LANG_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/build/my-languages.so"


def get_python_functions(file_path: str):
    """
    Loads a python file and parses each function name in the python file.

    Parameters
    ----------
    file_path : str
        file path to a python file

    Returns
    -------
    dict
        dict of function names found in the file
    """

    with open(file_path) as fp:
        source_code = fp.read()

    # Initialize the Python language
    PYTHON_LANGUAGE = Language(LANG_DIR, "python")
    parser = Parser()
    parser.set_language(PYTHON_LANGUAGE)

    tree = parser.parse(bytes(source_code, "utf-8"))
    root_node = tree.root_node

    # Traverse the AST to find function definitions
    for node in root_node.children:
        if node.type == "function_definition":
            function_start = node.start_byte
            function_end = node.end_byte
            function_body = source_code[function_start:function_end]

            yield function_body
