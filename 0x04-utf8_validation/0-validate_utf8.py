#!/usr/bin/python3


def validUTF8(data):
    num_bytes = 0  # Number of bytes to expect
    for byte in data:
        # Get the last 8 bits of the integer
        byte &= 0xFF

        # Determine the number of bytes in the character
        if num_bytes == 0:
            # Count leading 1s to determine the No. of bytes in this character
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
