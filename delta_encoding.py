def delta_encoding(data):
    if data is None:
        return []
    
    encoded = [data[0]]
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        encoded.append(diff)

    return encoded