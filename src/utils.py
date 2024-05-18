# src/utils.py

def is_valid_number(value):
    """
    Check if the provided value can be converted to a float.
    :param value: The value to check.
    :return: True if the value can be converted to a float, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def format_currency(value):
    """
    Format the provided value as a currency string.
    :param value: The value to format.
    :return: The formatted currency string.
    """
    return f"£{value:,.2f}"

def load_json_file(filepath):
    """
    Load data from a JSON file.
    :param filepath: Path to the JSON file.
    :return: Data loaded from the JSON file.
    """
    import json
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json_file(data, filepath):
    """
    Save data to a JSON file.
    :param data: Data to save.
    :param filepath: Path to the JSON file.
    :return: None
    """
    import json
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
