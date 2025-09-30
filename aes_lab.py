# AES Programming Lab
# Your Name: Luke GJ Potter

# Test with "ABCDEFGHIJKLMNOP"
# Should return:
# [[0x41, 0x45, 0x49, 0x4d],
#  [0x42, 0x46, 0x4a, 0x4e],
#  [0x43, 0x47, 0x4b, 0x4f],
#  [0x44, 0x48, 0x4c, 0x50]]
# Convert each character to its ASCII hex value
# Arrange in a 4x4 matrix using column-major order
# Return a 2D list of integers
def text_to_hex_matrix(plaintext):
    """Convert 16-character string to 4x4 hex matrix (column-major)"""
    if len(plaintext) != 16: raise ValueError("plaintext must be 16 character string")

    matrix = [[0 for _ in range(4)] for _ in range(4)]

    for i, char in enumerate(plaintext):
        row = i % 4
        col = i // 4
        matrix[row][col] = ord(char)

    return matrix


def sub_bytes(state_matrix):
    """Apply S-box substitution to each byte in the matrix"""
    # TODO: Implement this function
    pass


def shift_rows(state_matrix):
    """Perform row shifts on the state matrix"""
    # TODO: Implement this function
    pass


def add_round_key(state_matrix, round_key):
    """XOR state matrix with round key"""
    # TODO: Implement this function
    pass


def aes_round(plaintext, round_key):
    """Perform one complete AES round"""
    # TODO: Combine all functions
    pass


# Test your implementation
if __name__ == "__main__":
    plaintext = "HELLO WORLD!!!!!"  # Exactly 16 characters
    round_key = [
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ]

    result = aes_round(plaintext, round_key)
    print("Final encrypted matrix:", result)

    print(f"text_to_hex_matrix: {text_to_hex_matrix("ABCDEFGHIJKLMNOP")}")