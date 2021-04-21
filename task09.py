def show_vowels(word):
    vowels = []
    for letter in word.lower():
        if letter in ("aeiou"):
            if(letter not in vowels):
                vowels.append(letter)

    print(", ".join(vowels))