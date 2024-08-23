#!/usr/bin/python3
"""
This module validates if a given list of integers represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list of int): A list of integers where each integer represents a byte of data.
        
    Returns:
        bool: True if the data is a valid UTF-8 encoding, else False.
        
    Note:
        - UTF-8 encoding can be 1 to 4 bytes long.
        - Each integer in the list must be between 0 and 255 (inclusive).
    """
    n_bytes = 0

    for num in data:
        # Ensure the number is within the valid byte range
        if num < 0 or num > 255:
            return False

        # If this is the start of a new character sequence
        if n_bytes == 0:
            if num >> 5 == 0b110:  # 2-byte character
                n_bytes = 1
            elif num >> 4 == 0b1110:  # 3-byte character
                n_bytes = 2
            elif num >> 3 == 0b11110:  # 4-byte character
                n_bytes = 3
            elif num >> 7:  # Invalid 1-byte character (should start with 0)
                return False
        else:
            # This is a continuation byte, check if it starts with '10'
            if num >> 6 != 0b10:
                return False
            n_bytes -= 1

    # If n_bytes is not 0, it means there are missing continuation bytes
    return n_bytes == 0
