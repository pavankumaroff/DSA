def find_first_repeated_char(chars):
    seen = set()

    for char in chars:
        if char in seen:
            return char

        seen.add(char)

    return None


result = find_first_repeated_char("people")
print(result)


def find_first_non_repeated_char(chars):
    char_frequence = {}

    for char in chars:
        char_frequence[char] = char_frequence.get(char, 0) + 1

    for char in chars:
        if char_frequence[char] == 1:
            return char

    return None


result = find_first_non_repeated_char("people")
print(result)


def find_most_repeated_char(chars):
    char_frequence = {}

    for char in chars:
        char_frequence[char] = char_frequence.get(char, 0) + 1

    sorted_chars = sorted(
        char_frequence.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_chars[0][0] if len(sorted_chars) > 0 else None


result = find_most_repeated_char("peopleee")
print(result)
