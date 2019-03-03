# coding: utf-8
import click
from click.testing import CliRunner
from textutils import *



def test_reverse():
    runner = CliRunner()
    result = runner.invoke(reverse, ["-t", "ABCDE"])
    assert result.exit_code == 0
    assert result.output == "EDCBA\n"

    result = runner.invoke(reverse, ["-t", "012345"])
    assert result.exit_code == 0
    assert result.output == "543210\n"

    result = runner.invoke(reverse, ["--text", "aA0"])
    assert result.exit_code == 0
    assert result.output == "0Aa\n"

    result = runner.invoke(reverse, ["-f", "./test_data/test_reverse_01.txt"])
    assert result.exit_code == 0
    with open("test_reverse_01_result.txt") as f:
        _ = f.read()
        assert result.output == _

    result = runner.invoke(reverse, ["-file", "./test_data/test_reverse_02.txt"])
    assert result.exit_code == 0
    with open("test_reverse_02_result.txt") as f:
        _ = f.read()
        assert result.output == _


def main():
    test_reverse()

if __name__ == '__main__':
    main()
