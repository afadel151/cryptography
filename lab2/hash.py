from hashlib import sha256
from hashlib import sha1
from zlib import crc32

file_path = "text_to_hash.txt" 

def bit_difference_percentage(hash1_hex, hash2_hex):
    b1 = bin(int(hash1_hex, 16))[2:].zfill(len(hash1_hex) * 4)
    b2 = bin(int(hash2_hex, 16))[2:].zfill(len(hash2_hex) * 4)

    diff_bits = sum(1 for i in range(len(b1)) if b1[i] != b2[i])
    return (diff_bits /len(b1))*100 




try:
    with open(file_path, "rb") as file:
        content = file.read()

    first_hashed = sha256(content).hexdigest().upper()        
    print(first_hashed)

    
    byte_array = bytearray(content)
    # print(byte_array)
    byte_array[0] = (byte_array[0] + 1) % 256
    # print(byte_array)
    second_hashed = sha256(byte_array).hexdigest().upper()     
    print(second_hashed)
    print(bit_difference_percentage(first_hashed,second_hashed))


except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

    
