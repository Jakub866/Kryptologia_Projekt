def toAtBash(input_text):
    inputted_characters = list(input_text)
    result = ''

    alphabet = list("".join((chr(i) for i in range(128))))
    reverse_alphabet = list(reversed(alphabet))
    encryption_key = dict(zip(alphabet, reverse_alphabet))

    for character in inputted_characters:
        if character in encryption_key.keys():
            result += encryption_key.get(character)
        else:
            result += character
    return result
