"""
rules.py

Contains individual password evaluation rules.
Each rule returns a score delta and an optional issue message.
"""
def length_rule(password: str) -> tuple[int, str | None]:
    """
    Evaluates password length.
    """
    length = len(password)

    if length < 8:
        return -30, "Password is extremely short (less than 8 characters)"
    elif length < 12:
        return -15, "Password length is below the recommended 12 characters"
    elif length < 16:
        return 5, None
    else:
        return 15, None
    
def character_variety_rule(password: str) -> tuple[int, str | None]:
    """
    Checks for presence of uppercase, lowercase, digits, and symbols.
    """
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    categories = sum([has_lower, has_upper, has_digit, has_symbol])

    if categories <= 1:
        return -25, "Password uses only one character type"
    elif categories == 2:
        return -10, "Password lacks sufficient character variety"
    elif categories == 3:
        return 5, None
    else:
        return 15, None
    
def repeated_characters_rule(password: str) -> tuple[int, str | None]:
    """
    Penalizes excessive repeated characters.
    """
    if not password:
        return 0, None

    max_run = 1
    current_run = 1

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 1

    if max_run >= 4:
        return -15, "Password contains repeated characters"
    
    return 0, None

def sequential_characters_rule(password: str) -> tuple[int, str | None]:
    """
    Detects sequential characters like abc or 123.
    """
    sequences = "abcdefghijklmnopqrstuvwxyz0123456789"

    lowered = password.lower()

    for i in range(len(sequences) - 2):
        seq = sequences[i:i+3]
        if seq in lowered:
            return -20, "Password contains sequential characters (e.g. abc, 123)"

    return 0, None
