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


def main(args):
    embedding_cache = set_embedding_cache(args.ep)
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

    parser = argparse.ArgumentParser(description="Ayni: Chat with your codebase")
    parser.add_argument("-d", help="codebase root director", default=def_dir)
    parser.add_argument("-e", help="comma separate list of file extensions to search for. ex) .py,.go", default=def_ext)
    parser.add_argument("-p", help="Path to .pkl file where the embedding cache will be stored", default=embedding_path)
    parser.add_argument("-em", help="openai embedding model used to create embeddings", default=embedding_model)

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    load_dotenv(f"{os.getcwd()}/.env")  # take environment variables from .env.

    args = cli_args()

    openai_key = os.getenv("OPENAI_KEY")
    if openai_key is None:
        print("\033[91mError\033[0m: No OPENAI_KEY found in environment variables.")
        sys.exit(1)
    openai.api_key = openai_key

    main(args)
