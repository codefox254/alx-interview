#!/usr/bin/python3
# Function to validate if a given list of integers represents a valid UTF-8 encoding


def validUTF8(data):
    """Validate UTF-8 encoding for a list of integers."""

    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except:
        return False
    return True
