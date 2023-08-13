"""This module is concerned with code responsible for finding and parsing files.
"""

import os


def find_all_code(dir: str, exts: str):
    """
    Recursively search a directory for files that end with an extension from a
    given list of extensions.

    Parameters
    ----------
    dir : str
        the root directory to search
    exts: str
        comma separate list of file extensions to search for. ex) `".py,.go"`

    Yields
    ------
    str
        path to files
    """
    ext_list = [e.strip() for e in exts.split(",")]
    for root, _, files in os.walk(dir):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in ext_list:
                yield os.path.join(root, file)
