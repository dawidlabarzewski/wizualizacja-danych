def generuj(start = 1, count = 1, factor = 1):
    result = [start];
    current = start;

    for i in range(1, count):
        current *= factor
        result.append(current)

    return result