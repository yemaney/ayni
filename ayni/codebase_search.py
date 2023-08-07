"""This module is concerned with code responsible for finding and parsing files.
"""

import os


def find_all_code(dir: str, exts: list):
    """
    Recursively search a directory for files that end with an extension from a
    given list of extensions.

    Parameters
    ----------
    dir : str
        the root directory to search
    exts: list
        a list of file extensions to filter by

    Yields
    ------
    str
        path to files

    Raises
    ------
    ValueError
        if the passed `dir` is not a valid directory
    """
    if not os.path.isdir(dir):
        raise ValueError(f"{dir} is not a valid directory.")

    for root, _, files in os.walk(dir):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in exts:
                yield os.path.join(root, file)
