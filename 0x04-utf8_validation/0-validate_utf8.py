#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if the given data is a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes.

    Returns:
        bool: True if data is valid UTF-8 encoding, else False.
    """
    num_bytes = 0  # Number of bytes to expect

    for byte in data:
        # Get the last 8 bits of the integer
        byte &= 0xFF

        # Determine the number of bytes in the character
        if num_bytes == 0:
            # Count leading 1s to determine the no. of bytes in this character
            if (byte >> 7) == 0b0:  # 1-byte character
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid starting byte

        else:
            # Expect a continuation byte (must start with 10xxxxxx)
            if (byte >> 6) != 0b10:
                return False

        # If we used a byte for this character, reduce the count
        if num_bytes > 0:
            num_bytes -= 1

    return num_bytes == 0  # Check if we have finished all expected bytes
