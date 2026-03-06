import pytest
import foo_bar_baz as _m

# Access the function through the module each time so monkey-patching works
def fbz(n):
    return _m.foo_bar_baz(n)

# --- Return type ---

def test_return_type():
    assert isinstance(fbz(5), str)

# --- Edge cases ---

def test_n_zero():
    assert fbz(0) == ""

def test_n_one():
    assert fbz(1) == "1"

def test_n_negative():
    assert fbz(-1) == ""

# --- Small known sequences ---

def test_n_two():
    assert fbz(2) == "1 2"

def test_n_three():
    assert fbz(3) == "1 2 Foo"

def test_n_four():
    assert fbz(4) == "1 2 Foo 4"

def test_n_five():
    assert fbz(5) == "1 2 Foo 4 Bar"

def test_n_six():
    assert fbz(6) == "1 2 Foo 4 Bar Foo"

def test_n_ten():
    assert fbz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"

def test_n_fifteen():
    assert fbz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_n_twenty():
    assert fbz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"

def test_n_thirty():
    assert fbz(30) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    )

def test_n_forty_five():
    assert fbz(45) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz "
        "31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz"
    )

# --- Divisibility rules ---

def test_divisible_by_3_only():
    result = fbz(3).split()
    assert result[2] == "Foo"   # number 3

def test_divisible_by_5_only():
    result = fbz(5).split()
    assert result[4] == "Bar"   # number 5

def test_divisible_by_both_3_and_5():
    result = fbz(15).split()
    assert result[14] == "Baz"  # number 15 — not "FooBar"

def test_not_divisible_stays_as_number():
    result = fbz(7).split()
    assert result[0] == "1"
    assert result[1] == "2"
    assert result[3] == "4"
    assert result[6] == "7"

# --- Format checks ---

def test_space_delimited():
    tokens = fbz(10).split(" ")
    assert len(tokens) == 10

def test_no_leading_or_trailing_spaces():
    result = fbz(5)
    assert result == result.strip()

def test_single_spaces_between_tokens():
    assert len(fbz(15).split(" ")) == 15

# --- Comprehensive named test ---

def test_foo_bar_baz():
    assert fbz(0)  == ""
    assert fbz(1)  == "1"
    assert fbz(2)  == "1 2"
    assert fbz(3)  == "1 2 Foo"
    assert fbz(5)  == "1 2 Foo 4 Bar"
    assert fbz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert fbz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"
    assert fbz(30) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    )
    assert fbz(45) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz "
        "31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz"
    )
    # "Baz" must be used — not "FooBar" — for multiples of both 3 and 5
    tokens = fbz(45).split(" ")
    assert tokens[14] == "Baz"   # 15
    assert tokens[29] == "Baz"   # 30
    assert tokens[44] == "Baz"   # 45
    # Regular numbers unchanged
    assert tokens[0]  == "1"
    assert tokens[6]  == "7"
    assert tokens[15] == "16"
    assert tokens[18] == "19"
