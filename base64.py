BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(data):
    result = ""
    padding = ""

    # Convert each group of 3 bytes into 4 Base64 characters
    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]
        # Convert bytes to an integer
        chunk_int = int.from_bytes(chunk, "big")
        # Extract 6 bits at a time and map to Base64 characters
        for j in range(18, -1, -6):
            index = (chunk_int >> j) & 0x3F
            result += BASE64_CHARS[index]
        padding = "=" * (3 - len(chunk) % 3)

    return result + padding


if __name__ == "__main__":
    user_input = input("Enter data to encode: ").encode('utf-8')
    encoded_data = base64_encode(user_input)
    print("Base64 encoded data:", encoded_data)
