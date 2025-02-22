def alternate(s):
    c = list(set(s))
    combination = []
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            combination.append([c[i], c[j]])

    max_length = 0
    for k in combination:
        new_string = []
        for i in range(len(s)):
            if s[i] in k:
                if len(new_string) > 0 and new_string[-1] == s[i]:
                    new_string = []
                    break
                new_string.append(s[i])
        max_length = max(max_length, len(new_string))

    return max_length
