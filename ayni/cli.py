"""This module is concerned with code responsible for the main cli.
"""

import argparse
import os

from dotenv import load_dotenv

from ayni.codebase_search import find_all_code
from ayni.parse import get_python_functions


def main(dir, ext):
    for f in find_all_code(dir, ext):
        funcs = get_python_functions(f)
        print(f"file:{f} has functions: {funcs}")


if __name__ == "__main__":
    load_dotenv(f"{os.getcwd()}/.env")  # take environment variables from .env.

    def_dir = os.getenv("AYNI_DIR")
    def_ext = os.getenv("AYNI_EXTENSIONS")

    parser = argparse.ArgumentParser(description="Ayni: Chat with your codebase")
    parser.add_argument("dir", nargs="?", help="codebase root director", default=def_dir)
    parser.add_argument(
        "-e", "--extensions", help="comma separate list of file extensions to search for. ex) .py,.go", default=def_ext
    )
    args = parser.parse_args()
    main(args.dir, args.extensions)
