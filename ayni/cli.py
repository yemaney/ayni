import argparse
import os

from dotenv import load_dotenv

from ayni.codebase_search import find_all_code


def main():
    load_dotenv()  # take environment variables from .env.

    def_dir = os.getenv("AYNI_DIR")
    def_ext = os.getenv("AYNI_EXTENSIONS")

    parser = argparse.ArgumentParser(description="Ayni: Chat with your codebase")
    parser.add_argument("dir", nargs="?", help="codebase root director", default=def_dir)
    parser.add_argument(
        "-e", "--extensions", help="comma separate list of file extensions to search for. ex) .py,.go", default=def_ext
    )
    args = parser.parse_args()

    for f in find_all_code(args.dir, args.extensions):
        print(f)


if __name__ == "__main__":
    main()
