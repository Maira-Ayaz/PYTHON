def group_anagrams(strs):
    d = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in d:
            d[key] = []

        d[key].append(word)

    return list(d.values())


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))