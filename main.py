from delta_encoding import *
from delta_decoding import *
from bitpacking import *
from bitunpacking import *
from huffman_encoding import *
from huffman_decoding import *


data = [100, 122, 213]
print(data)
encoded = delta_encoding(data)
print(encoded)
max_value = max(encoded)
print(max_value)
bit_per_value = max_value.bit_length()
print(bit_per_value)
bitstream = bit_packing(encoded, bit_per_value)
print(bitstream)
print(len(bitstream))
def chunk_string(bitstream, chunk_size):
    chunks = []
    for i in range(0, len(bitstream), chunk_size):
        chunk = bitstream[i:i + chunk_size]
        chunks.append(chunk)
    return chunks
chunks = chunk_string(bitstream, len(bitstream) // 2)
print(chunks)
frequencies = get_frequencies(chunks)
print(frequencies)
tree_root = build_huffman_tree(frequencies)
codes = generate_codes(tree_root)
print(codes)
encoded_list = encode_list(chunks, codes)
print(encoded_list)
print(len(encoded_list))
print("-----------------------------------------------------")
decoded_list = huffman_decoded_list(encoded_list, tree_root)
print(decoded_list)
print(len(decoded_list))
unpacked = bit_unpack(decoded_list, bit_per_value)
print(unpacked)
final_decoded = delta_decoding(unpacked)
print(final_decoded)
print("-----------------------------------------------------")
original_bits = len(data) * 8  # each number stored as 8 bits originally
compressed_bits = len(encoded_list)  # already a bitstring

compression_ratio = original_bits / compressed_bits
compression_percentage = ((original_bits - compressed_bits) / original_bits) * 100

print(f"Original Size: {original_bits} bits")
print(f"Compressed Size: {compressed_bits} bits")
print(f"Compression Ratio: {compression_ratio:.2f}")
print(f"Compression Percentage: {compression_percentage:.2f}%")
