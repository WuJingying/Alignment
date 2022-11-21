'''import Levenshtein
str1 = 'hello'
str2 = 'world'
print(Levenshtein.ratio(str1, str2))'''


def LevenDistance(str1, str2):
    if not str1:
        return len(str2 or '') or 0
    if not str2:
        return len(str1 or '') or 0

    size1 = len(str1)
    size2 = len(str2)

    last = 0
    tmp = list(range(size2 + 1))
    value = None

    for i in range(size1):
        tmp[0] = i + 1
        last = i
        for j in range(size2):
            if str1[i] == str2[j]:
                value = last
            else:
                value = 1 + min(last, tmp[j], tmp[j+1])
            last = tmp[j+1]
            tmp[j+1] = value
    return value

if __name__ == '__main__':
    str1 = 'hello'
    str2 = 'world'
    print(LevenDistance(str1, str2))
