"""This is a utility python script used to build the c extension files for ayni.
"""

from tree_sitter import Language

Language.build_library(
    # Store the library in the `build` directory
    "ayni/build/my-languages.so",
    # Include one or more languages
    ["tree-sitter-python"],
)
