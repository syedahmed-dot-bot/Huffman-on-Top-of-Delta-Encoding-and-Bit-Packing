def huffman_decoded_list(encoded_data, root):
    decoded = ''
    current = root

    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.element is not None:
            decoded += current.element
            current = root

    return decoded