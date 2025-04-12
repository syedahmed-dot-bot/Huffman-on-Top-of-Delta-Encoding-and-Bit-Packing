def delta_decoding(unpacked):
    if unpacked is None:
        return []
    
    decoded = [unpacked[0]]

    for i in range(1, len(unpacked)):
        sum = decoded[-1] + unpacked[i]
        decoded.append(sum)

    return decoded