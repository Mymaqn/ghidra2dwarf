#!/usr/bin/env python3

from util import *


def test_function():
    execute_cmd("-file-exec-and-symbols ./test_dbg")
    execute_cmd("set listsize 1")
    execute_cmd("-break-insert 136")
    execute_cmd("-break-insert 142")
    execute_cmd("-exec-run")

    execute_cmd("c 2")
    assert 2 == get_int("i")
    assert "i = i + 1;" == get_line(136)

    execute_cmd("c 3")
    d = get_struct("*ex_2")
    assert "15" == d["x"]
    assert "20" == d["y"]
    assert "Example 1" in d["name"]

    assert 15 == get_int("ex_2->x")


test_function()
