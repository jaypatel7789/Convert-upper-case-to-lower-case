def convert_to_lowercase(input_str):
    """
    Convert a string with upper case characters into lower case.

    Parameters:
    input_str (string): The string that contains upper case characters.

    Returns:
    string: A new string where all the upper case characters have been converted to lower case.
    """
    # Using the built-in lower() function to convert all characters to lower case
    return input_str.lower()

# Test the function
original_str = "Hello, World!"
print("Original:", original_str)

lowercase_str = convert_to_lowercase(original_str)
print("Lowercase:", lowercase_str)
