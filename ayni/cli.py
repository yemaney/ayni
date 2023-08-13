"""This module is concerned with code responsible for the main cli.
"""

import argparse
import os
import sys
from argparse import Namespace

import openai
from dotenv import load_dotenv

from ayni.cache import cache_embedding, set_embedding_cache
from ayni.codebase_search import find_all_code
from ayni.parse import get_python_functions
from ayni.types import Extension


def main(args):
    embedding_cache = set_embedding_cache(args.p)
    for f in find_all_code(args.d, args.e):
        for func in get_python_functions(f):
            cache_embedding(func, embedding_cache, args.p, args.em)


def cli_args() -> Namespace:
    """cli_args gathers the arguements to be passed to the main functions

    Returns
    -------
    Namespace
        contains the arguements passed to the cli
    """
    def_dir = os.getenv("AYNI_DIR")
    def_ext = os.getenv("AYNI_EXTENSIONS")
    embedding_path = os.getenv("AYNI_EMBEDDING_PATH", "embeddings_cache.pkl")
    embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002")
    openai_key = os.getenv("OPENAI_KEY")

    parser = argparse.ArgumentParser(description="Ayni: Chat with your codebase")
    parser.add_argument("-d", help="codebase root director", default=def_dir)
    parser.add_argument("-e", help="comma separate list of file extensions to search for. ex) .py,.go", default=def_ext)
    parser.add_argument("-p", help="Path to .pkl file where the embedding cache will be stored", default=embedding_path)
    parser.add_argument("-em", help="openai embedding model used to create embeddings", default=embedding_model)
    parser.add_argument("-k", help="openai api key", default=openai_key)

    args = parser.parse_args()
    return args


def catch_arg_errors(args: Namespace):
    """catch_arg_errors validates the parameters passed to an argsparse Namespace, if any
    parameters fail a check, then an error message is printed and the system exits with code 1.

    Parameters
    ----------
    args : Namespace
        arguements that are passed to the cli
    """
    if not os.path.isdir(args.d):
        print(f"\033[91mERROR\033[0m: {args.d} is not a valid directory.")
        sys.exit(1)

    ext_list = [e.strip() for e in args.e.split(",")]
    for ext in ext_list:
        try:
            Extension(ext)
        except ValueError:
            print(f"\033[91mERROR\033[0m: {ext}. is not a valid Extension")
            sys.exit(1)

    folder_path = os.path.dirname(args.p)
    if not os.path.exists(folder_path):
        print(f"\033[91mERROR\033[0m: {folder_path} is not a valid directory.")
        sys.exit(1)

    if args.k is None:
        print("\033[91mERROR\033[0m: No OPENAI_KEY found in environment variables.")
        sys.exit(1)
    openai.api_key = args.k


if __name__ == "__main__":
    load_dotenv(f"{os.getcwd()}/.env")  # take environment variables from .env.

    args = cli_args()
    catch_arg_errors(args)

    main(args)
