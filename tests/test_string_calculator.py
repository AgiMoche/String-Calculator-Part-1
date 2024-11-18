import pytest

from string_calculator.string_calculator import (
    add,
    parse_input_string,
    check_user_input_type,
    check_negative_numbers,
    check_for_delimeter_type,
)


def test_check_negative_numbers():
    with pytest.raises(ValueError, match="negatives not allowed -1,-2"):
        check_negative_numbers("-1,-2,3,4")


def test_check_user_input_type_with_no_string_parameter():
    with pytest.raises(
        TypeError,
        match="The input provided is invalid. Provide only a string as the input",
    ):
        check_user_input_type([123, 1, 2])


def test_parse_input_string_with_non_integer_delimeter_at_the_start_of_input():
    with pytest.raises(
        ValueError,
        match="Invalid input",
    ):
        parse_input_string("//***\n***1***2***3***")


def test_check_for_delimeter_type_with_no_delimeter():
    assert check_for_delimeter_type("1,2,3,4") == ["1", "2", "3", "4"]


def test_parse_input_string_with_standard_input():
    assert parse_input_string("//4\n142") == ["1", "2"]


def test_parse_input_string_with_delimeter_repeated():
    with pytest.raises(ValueError, match="Invalid input"):
        parse_input_string("//88\n18882")


def test_parse_input_string_with_delimeter_at_the_start_of_input():
    with pytest.raises(ValueError, match="Invalid input"):
        parse_input_string("//4\n434243")


def test_parse_input_string_with_delimeter_at_the_end_of_input():
    with pytest.raises(ValueError, match="Invalid input"):
        parse_input_string("//4\n342434")


def test_parse_input_string_with_delimeter_at_both_ends_of_input():
    with pytest.raises(ValueError, match="Invalid input"):
        parse_input_string("//4\n4342434")


def test_add_with_standard_input():
    assert add("1,2,3,4") == 10


def test_add_with_new_line_delimeter():
    assert add("1\n2,3") == 6


def test_add_with_one_input():
    assert add("123") == 123


def test_add_with_no_input():
    assert add("") == 0


def test_add_with_delimeter_as_the_only_input():
    assert add("//;\n") == 0


def test_add_with_number_as_delimeter():
    assert add("//4\n142") == 3


def test_add_with_non_integer_as_delimeter():
    assert add("//;\n1;2") == 3


def test_add_with_delimeter_having_any_length():
    assert add("//***\n1***2***3") == 6


def test_custom_delimiter_88_input_1_20_3():
    assert add("//88\n18820883") == 24


def test_custom_delimiter_star_star_star_semicolon_input_1_2_3():
    assert add("//;\n1;2***;3") == 6
