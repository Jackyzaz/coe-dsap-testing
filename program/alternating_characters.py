def alternatingCharacters(string):
    current = string[0]
    count = 0
    for i in range(1, len(string)):
        if current == string[i]:
            count += 1
            continue
        else:
            current = string[i]

    return count
