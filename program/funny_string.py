def funnyString(string):
    ascii_string = list(map(ord, string))
    ascii_string_dif = []
    for i in range(1, len(ascii_string)):
        ascii_string_dif.append(abs(ascii_string[i] - ascii_string[i - 1]))

    reverse_ascii_string = ascii_string[::-1]
    for j in range(1, len(reverse_ascii_string)):
        if (
            abs(reverse_ascii_string[j] - reverse_ascii_string[j - 1])
            != ascii_string_dif[j - 1]
        ):
            return "Not Funny"

    return "Funny"
