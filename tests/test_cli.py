from argparse import Namespace

import pytest

from ayni.cli import catch_arg_errors


def test_catch_arg_errors(capsys, test_directory):
    args = Namespace(d=f"{test_directory}/none")
    assert_error(capsys, args, f"\033[91mERROR\033[0m: {args.d} is not a valid directory.\n")

    args = Namespace(d=f"{test_directory}", e=".pyc")
    assert_error(capsys, args, f"\033[91mERROR\033[0m: {args.e}. is not a valid Extension\n")

    args = Namespace(d=f"{test_directory}", e=".py", p=f"{test_directory}/none/")
    assert_error(capsys, args, f"\033[91mERROR\033[0m: {args.p[:len(args.p)-1]} is not a valid directory.\n")

    args = Namespace(d=f"{test_directory}", e=".py", p=f"{test_directory}/", k=None)
    assert_error(capsys, args, "\033[91mERROR\033[0m: No OPENAI_KEY found in environment variables.\n")


def assert_error(capsys, args, error_msg):
    with pytest.raises(SystemExit) as exc_info:
        catch_arg_errors(args)

    captured = capsys.readouterr()
    captured_out = captured.out

    assert captured_out == error_msg
    assert exc_info.value.code == 1
