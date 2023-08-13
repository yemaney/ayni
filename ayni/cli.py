"""This module is concerned with code responsible for the main cli.
"""

import argparse
import os
import sys

import openai
from dotenv import load_dotenv

from ayni.cache import cache_embedding, set_embedding_cache
from ayni.codebase_search import find_all_code
from ayni.parse import get_python_functions


def main(dir, ext):
    embedding_cache = set_embedding_cache()
    for f in find_all_code(dir, ext):
        for func in get_python_functions(f):
            cache_embedding(func, embedding_cache)


if __name__ == "__main__":
    load_dotenv(f"{os.getcwd()}/.env")  # take environment variables from .env.

    def_dir = os.getenv("AYNI_DIR")
    def_ext = os.getenv("AYNI_EXTENSIONS")
    openai_key = os.getenv("OPENAI_KEY")
    if openai_key is None:
        print("\033[91mError\033[0m: No OPENAI_KEY found in environment variables.")
        sys.exit(1)

    openai.api_key = openai_key

    parser = argparse.ArgumentParser(description="Ayni: Chat with your codebase")
    parser.add_argument("dir", nargs="?", help="codebase root director", default=def_dir)
    parser.add_argument(
        "-e", "--extensions", help="comma separate list of file extensions to search for. ex) .py,.go", default=def_ext
    )
    args = parser.parse_args()
    main(args.dir, args.extensions)
