def toAtBash(text):
    characters = list(text)
    result =''
    for character in characters:
        if character in code_dictionary:
            result += code_dictionary.get(character)
        else:
            result+= character

    #print(f"weszlo jako {characters} wyszlo jako {result}")
    return result


alphabet = list("".join((chr(i) for i in range(128))))
reverse_alphabet = list(reversed(alphabet))

code_dictionary = dict(zip(alphabet, reverse_alphabet))


