CUSTOM_ALPHABET = "ybndrfg8ejkmcpqxot1uwisza345h769"
P_PREFIX = "m7xzr7muqtxsr3m8pfzf6h5ep738ez5ncftss7d1cftskz49qj4zg7n9cizgez5upbzzr7n9cjosg45wqjosg3mu"

def custom_base32_decode(encoded_string, alphabet):
    if len(alphabet) != 32:
        raise ValueError("Alphabet length must be 32 for Base32")

    char_to_val = {char: i for i, char in enumerate(alphabet)}
    
    bits = ""
    for char_code in encoded_string:
        if char_code not in char_to_val:
            raise ValueError(f"Character '{char_code}' not in custom alphabet!")
        val = char_to_val[char_code]
        bits += format(val, '05b') 

    decoded_bytes = bytearray()
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:

            print(f"Warning: Trailing bits '{byte_bits}' might be incomplete.")
            continue 
        decoded_bytes.append(int(byte_bits, 2))
        
    return decoded_bytes

try:
    decoded_data = custom_base32_decode(P_PREFIX, CUSTOM_ALPHABET)
    print(f"Decoded data (length {len(decoded_data)} bytes): {decoded_data}")
    try:
        print(f"Decoded data as string: {decoded_data.decode('utf-8')}")
    except UnicodeDecodeError:
        print("Decoded data is not valid UTF-8, showing hex:")
        print(f"Decoded data as hex: {decoded_data.hex()}")

except ValueError as e:
    print(f"Error: {e}")