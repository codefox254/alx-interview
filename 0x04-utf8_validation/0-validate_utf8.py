#!/usr/bin/python3

def validUTF8(data):
    number_of_bytes = 0

    for num in data:
        # Get the 8 least significant bits of the number
        byte = num & 0xFF

        if number_of_bytes == 0:
            # Check how many 1's are at the start of the byte
            if (byte >> 5) == 0b110:  # 2-byte character
                number_of_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                number_of_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                number_of_bytes = 3
            elif (byte >> 7):  # 1-byte character but MSB is not 0
                return False
        else:
            # Check that this byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
            number_of_bytes -= 1

    # All characters should be fully processed
    return number_of_bytes == 0
