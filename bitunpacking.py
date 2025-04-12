def bit_unpack(bitstream, bit_per_value):
    unpacked = []

    for i in range (0, len(bitstream), bit_per_value):
        number = bitstream[i : i + bit_per_value]
        value = int(number, 2)
        unpacked.append(value)
    
    return unpacked