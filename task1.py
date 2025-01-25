def convert_vowels_to_upper(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in word:
        if char.lower() in vowels:
            result += char.upper()
        else:
            result += char
    return result



print(convert_vowels_to_upper("hello"))
print(convert_vowels_to_upper("aabbgg"))