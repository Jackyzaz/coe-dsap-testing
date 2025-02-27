def caesar_cipher(string, k):
    umap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lmap = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for s in string:
        if s.isupper():
            original_index = umap.index(s)
            new_index = (k + original_index) % 26
            new_string += umap[new_index]
        elif s.islower():
            original_index = lmap.index(s)
            new_index = (k + original_index) % 26
            new_string += lmap[new_index]
        else:
            new_string += s
    return new_string
