def count_vowel(s):
    total = 0
    for a in s:
        if a in "aeiouAEIOU":
            total = total + 1
    return total

print(count_vowel("maira"))