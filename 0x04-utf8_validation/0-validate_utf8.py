#!/usr/bin/python3
# Function to validate if a given list of integers represents a valid UTF-8 encoding


def validUTF8(data):
    """Validate UTF-8 encoding for a list of integers."""

    # This variable keeps track of the number of expected continuation bytes.
    n_bytes = 0

    
    for num in data:
        # If we're not expecting any continuation bytes, determine how many bytes the character uses.
        if n_bytes == 0:
            # Check the number of leading 1's to determine the number of bytes.
            if num >> 5 == 0b110:  # Character spans 2 bytes.
                n_bytes = 1
            elif num >> 4 == 0b1110:  # Character spans 3 bytes.
                n_bytes = 2
            elif num >> 3 == 0b11110:  # Character spans 4 bytes.
                n_bytes = 3
            elif num >> 7:  # Invalid if leading bit is 1 and doesn't match any valid UTF-8 pattern.
                return False
        else:
            # Check if this byte is a valid continuation byte (should start with '10').
            if num >> 6 != 0b10:
                return False
            # Decrement the number of expected continuation bytes.
            n_bytes -= 1

    
    # After processing all data, ensure there are no leftover expected continuation bytes.
    return n_bytes == 0


# Example usage
if __name__ == "__main__":
    data = [197, 130, 1]
    print(validUTF8(data))  # Expected output: True

    data = [235, 140, 4]
    print(validUTF8(data))  # Expected output: False
