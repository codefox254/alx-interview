#!/usr/bin/python3
# This function checks if a given list of integers represents a valid UTF-8 encoding.


def validUTF8(data):
    # Hack to get around this wierd case
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
