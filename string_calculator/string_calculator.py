import re


def check_user_input_type(input_string):
    if not isinstance(input_string, str):
        raise TypeError(
            "The input provided is invalid. Provide only a string as the input"
        )


def parse_input_string(input_string):
    default_delimeter = input_string[2]
    values_in_user_input = [
        value
        for value in re.split(rf"[^{default_delimeter}\d]", input_string)
        if len(value) > 0
    ]

    if len(values_in_user_input) == 1:
        return [0]

    full_default_delimeter = values_in_user_input[0]
    user_input_with_delimeter = "".join(values_in_user_input[1:])

    if user_input_with_delimeter.isdigit():
        if re.search(f"^{default_delimeter}", user_input_with_delimeter) or re.search(
            f"{default_delimeter}$", user_input_with_delimeter
        ):
            raise ValueError("Invalid input")

        values_in_user_input_without_delimeter = [
            value
            for value in re.split(
                f"{full_default_delimeter}", user_input_with_delimeter
            )
            if len(value) > 0
        ]

        for value in values_in_user_input_without_delimeter:
            if default_delimeter in value:
                raise ValueError("Invalid input")

    if not (user_input_with_delimeter.isdigit()):
        if re.search(f"^[{default_delimeter}]", user_input_with_delimeter) or re.search(
            f"[{default_delimeter}]$", user_input_with_delimeter
        ):
            raise ValueError("Invalid input")

    values_in_user_input_without_delimeter = [
        value
        for value in re.split(rf"[{full_default_delimeter}]", user_input_with_delimeter)
        if len(value) > 0
    ]

    return values_in_user_input_without_delimeter


def check_negative_numbers(input_string):
    negatives_in_user_input = []

    for number in input_string.split(","):
        if int(number) < 0:
            negatives_in_user_input.append(number)

    raise ValueError(f"negatives not allowed {','.join(negatives_in_user_input)}")


def check_for_delimeter_type(input_string):
    if re.search("^//", input_string):
        return parse_input_string(input_string)

    elif "-" in input_string:
        check_negative_numbers(input_string)

    else:
        values_in_user_input = re.split(r"\D", input_string)
        return [value for value in values_in_user_input if value.isdigit()]


def add(input_string):
    check_user_input_type(input_string)
    check_for_delimeter_type(input_string)

    return sum([int(number) for number in check_for_delimeter_type(input_string)])
