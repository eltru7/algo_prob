def length_of_longest_substring(substring):

    letters = {}
    count = 0
    i = 0

    for j in range(len(substring)):
        if substring[j] in letters:
            i = max(letters[substring[j]], i)

        count = max(count, j - i + 1)
        letters[substring[j]] = j + 1

    return count
