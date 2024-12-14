def is_string_integer(char):
    """
    Check if a given single character represents a valid integer in base 10.

    Args:
        char (str): A single character string to be checked.

    Returns:
        bool: True if the character is a digit (0-9), False otherwise.

    Raises:
        AssertionError: If the input is not a single character.
    """
    # Ensure the input is a single character
    assert (
        isinstance(char, str) and len(char) == 1
    ), "Input must be a single character string."

    # Check if the character is a digit
    return char.isdigit()
