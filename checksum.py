def checksum(data):
    """
    Calculates the checksum of the given data.
    """
    total = sum(ord(character) for character in data)
    return total & 0xFF  # Take the least significant byte

def add_checksum(data):
    """
    Adds the checksum to the given data.
    """
    chksum = checksum(data)
    return data + chr(chksum)

def verify_checksum(data_with_checksum):
    """
    Verifies the checksum of the given data with checksum appended.
    """
    data = data_with_checksum[:-1]  # Remove the last character (checksum)
    expected_checksum = checksum(data)
    actual_checksum = ord(data_with_checksum[-1])  # Last character is the checksum
    return expected_checksum == actual_checksum

if __name__ == "__main__":
    data = "Hello, world!"
    data_with_checksum = add_checksum(data)
    print("Original data:", data)
    print("Data with checksum:", data_with_checksum)
    print("Checksum verification:", verify_checksum(data_with_checksum))
