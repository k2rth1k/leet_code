def permutation(combo: str):
    length = len(combo)
    for i in range(length):
        for j in range(length):
            swap(combo, i, j)
        pass
    pass


def swap(combo: str, i, j):
    temp = combo[i]
    combo[i] = combo[j]
    combo[j] = temp
