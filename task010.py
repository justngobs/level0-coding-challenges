def show_common(word_one, word_two):
    common = []
    for letter in word_one.lower():
        if letter in word_two.lower():
            if(letter not in common):
                common.append(letter)

    print("Common letters: " + ", ".join(common))