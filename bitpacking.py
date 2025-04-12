def bit_packing(encoded, bit_per_value):
    bitstream= ''

    for value in encoded:
        binary= format(value, f'0{bit_per_value}b')
        bitstream += binary

    return bitstream