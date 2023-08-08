from ayni.cli import main


def test_cli(capsys, test_directory):
    main(f"{test_directory}", ".py")
    captured = capsys.readouterr()

    assert (
        captured.out
        == f"""file:{test_directory}/file2.py has functions: ['func1', 'func2', 'func3']
file:{test_directory}/subdir/file3.py has functions: []
"""
    )
