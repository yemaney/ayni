import argparse

from ayni.codebase_search import find_all_code


def main():
    parser = argparse.ArgumentParser(description="Ayni: Chat with your codebase")
    parser.add_argument("dir", help="codebase root director")
    parser.add_argument("-e", "--extensions", help="comma seperate list of file extensions to search for. ex) .py,.go")
    args = parser.parse_args()

    for f in find_all_code(args.dir, args.extensions):
        print(f)
