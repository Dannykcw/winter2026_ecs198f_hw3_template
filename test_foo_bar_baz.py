import pytest

from foo_bar_baz import foo_bar_baz

# --- Return type ---

def test_return_type():
    assert isinstance(foo_bar_baz(5), str)

# --- Edge cases ---

def test_n_zero():
    assert foo_bar_baz(0) == ""

def test_n_one():
    assert foo_bar_baz(1) == "1"

# --- Small known sequences ---

def test_n_three():
    assert foo_bar_baz(3) == "1 2 Foo"

def test_n_five():
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

def test_n_fifteen():
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(15) == expected

# --- Divisibility rules ---

def test_divisible_by_3_only():
    # 3 is divisible by 3 but not 5 → "Foo"
    result = foo_bar_baz(3).split()
    assert result[2] == "Foo"   # index 2 = number 3

def test_divisible_by_5_only():
    # 5 is divisible by 5 but not 3 → "Bar"
    result = foo_bar_baz(5).split()
    assert result[4] == "Bar"   # index 4 = number 5

def test_divisible_by_both_3_and_5():
    # 15 is divisible by both → "Baz"
    result = foo_bar_baz(15).split()
    assert result[14] == "Baz"  # index 14 = number 15

def test_not_divisible_stays_as_number():
    # 1, 2, 4, 7 are not divisible by 3 or 5
    result = foo_bar_baz(7).split()
    assert result[0] == "1"
    assert result[1] == "2"
    assert result[3] == "4"
    assert result[6] == "7"

# --- Format checks ---

def test_space_delimited():
    # tokens should equal n elements
    result = foo_bar_baz(10)
    tokens = result.split(" ")
    assert len(tokens) == 10

def test_no_leading_or_trailing_spaces():
    result = foo_bar_baz(5)
    assert result == result.strip()

def test_single_spaces_between_tokens():
    result = foo_bar_baz(15)
    # splitting on single space should give exactly n tokens
    assert len(result.split(" ")) == 15

# --- Additional exact string checks ---

def test_n_two():
    assert foo_bar_baz(2) == "1 2"

def test_n_four():
    assert foo_bar_baz(4) == "1 2 Foo 4"

def test_n_six():
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"

def test_n_ten():
    assert foo_bar_baz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"

def test_n_twenty():
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"
    assert foo_bar_baz(20) == expected

# --- Larger exact string checks ---

def test_n_thirty():
    expected = (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    )
    assert foo_bar_baz(30) == expected

def test_n_forty_five():
    expected = (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz "
        "31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz"
    )
    assert foo_bar_baz(45) == expected

# --- Negative n ---

def test_n_negative():
    assert foo_bar_baz(-1) == ""

# --- Comprehensive named test ---

def test_foo_bar_baz():
    # Exact outputs for a range of n values
    assert foo_bar_baz(0)  == ""
    assert foo_bar_baz(1)  == "1"
    assert foo_bar_baz(2)  == "1 2"
    assert foo_bar_baz(3)  == "1 2 Foo"
    assert foo_bar_baz(5)  == "1 2 Foo 4 Bar"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"
    assert foo_bar_baz(30) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    )
    assert foo_bar_baz(45) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz "
        "31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz"
    )
    # "Baz" for multiples of both 3 and 5 — not "FooBar"
    tokens = foo_bar_baz(45).split(" ")
    assert tokens[14] == "Baz"   # 15
    assert tokens[29] == "Baz"   # 30
    assert tokens[44] == "Baz"   # 45
    # Regular numbers unchanged
    assert tokens[0]  == "1"
    assert tokens[6]  == "7"
    assert tokens[15] == "16"
    assert tokens[18] == "19"