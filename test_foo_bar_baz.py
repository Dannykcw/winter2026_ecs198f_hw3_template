import pytest
import foo_bar_baz as _m

# Access the function through the module each time so monkey-patching works
def fbz(n):
    return _m.foo_bar_baz(n)

# ---------------------------------------------------------------------------
# Return type
# ---------------------------------------------------------------------------

def test_return_type():
    assert isinstance(fbz(5), str)

# ---------------------------------------------------------------------------
# Edge cases: n <= 0
# ---------------------------------------------------------------------------

def test_n_negative():
    assert fbz(-1) == ""

def test_n_zero():
    assert fbz(0) == ""

# ---------------------------------------------------------------------------
# Exact string for every n from 1 to 20
# ---------------------------------------------------------------------------

def test_n_1():
    assert fbz(1) == "1"

def test_n_2():
    assert fbz(2) == "1 2"

def test_n_3():
    assert fbz(3) == "1 2 Foo"

def test_n_4():
    assert fbz(4) == "1 2 Foo 4"

def test_n_5():
    assert fbz(5) == "1 2 Foo 4 Bar"

def test_n_6():
    assert fbz(6) == "1 2 Foo 4 Bar Foo"

def test_n_7():
    assert fbz(7) == "1 2 Foo 4 Bar Foo 7"

def test_n_8():
    assert fbz(8) == "1 2 Foo 4 Bar Foo 7 8"

def test_n_9():
    assert fbz(9) == "1 2 Foo 4 Bar Foo 7 8 Foo"

def test_n_10():
    assert fbz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"

def test_n_11():
    assert fbz(11) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11"

def test_n_12():
    assert fbz(12) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo"

def test_n_13():
    assert fbz(13) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13"

def test_n_14():
    assert fbz(14) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14"

def test_n_15():
    assert fbz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_n_16():
    assert fbz(16) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16"

def test_n_17():
    assert fbz(17) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17"

def test_n_18():
    assert fbz(18) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo"

def test_n_19():
    assert fbz(19) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19"

def test_n_20():
    assert fbz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"

# ---------------------------------------------------------------------------
# Larger exact string checks
# ---------------------------------------------------------------------------

def test_n_30():
    assert fbz(30) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    )

def test_n_45():
    assert fbz(45) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz "
        "31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz"
    )

def test_n_60():
    assert fbz(60) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz "
        "31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz "
        "46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 Baz"
    )

# ---------------------------------------------------------------------------
# Divisibility rules
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Format checks
# ---------------------------------------------------------------------------

def test_space_delimited():
    tokens = fbz(10).split(" ")
    assert len(tokens) == 10

def test_no_leading_or_trailing_spaces():
    result = fbz(5)
    assert result == result.strip()

def test_single_spaces_between_tokens():
    assert len(fbz(15).split(" ")) == 15

# ---------------------------------------------------------------------------
# Comprehensive named test
# ---------------------------------------------------------------------------

def test_foo_bar_baz():
    # Every n from 0 to 20
    assert fbz(0)  == ""
    assert fbz(1)  == "1"
    assert fbz(2)  == "1 2"
    assert fbz(3)  == "1 2 Foo"
    assert fbz(4)  == "1 2 Foo 4"
    assert fbz(5)  == "1 2 Foo 4 Bar"
    assert fbz(6)  == "1 2 Foo 4 Bar Foo"
    assert fbz(7)  == "1 2 Foo 4 Bar Foo 7"
    assert fbz(8)  == "1 2 Foo 4 Bar Foo 7 8"
    assert fbz(9)  == "1 2 Foo 4 Bar Foo 7 8 Foo"
    assert fbz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"
    assert fbz(11) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11"
    assert fbz(12) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo"
    assert fbz(13) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13"
    assert fbz(14) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14"
    assert fbz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert fbz(16) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16"
    assert fbz(17) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17"
    assert fbz(18) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo"
    assert fbz(19) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19"
    assert fbz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"
    # Larger values
    assert fbz(30) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    )
    assert fbz(60) == (
        "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz "
        "16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz "
        "31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz "
        "46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 Baz"
    )
    # "Baz" for multiples of both 3 and 5 — never "FooBar"
    tokens = fbz(60).split(" ")
    assert tokens[14] == "Baz"   # 15
    assert tokens[29] == "Baz"   # 30
    assert tokens[44] == "Baz"   # 45
    assert tokens[59] == "Baz"   # 60
    # Regular numbers unchanged
    assert tokens[0]  == "1"
    assert tokens[6]  == "7"
    assert tokens[10] == "11"
    assert tokens[15] == "16"
