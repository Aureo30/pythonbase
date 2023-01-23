# voyelle : a, e, i, o, u, y

def get_vowels(vowels_count):
    vowel = 0

    for i in vowels_count:
        if i in ["a", "e", "i", "o", "u", "y"]:
            vowel += 1
    return vowel


word = input("Entrer un mot/phrase ")
vowels_count = get_vowels(word)
print("Il y a", vowels_count, "voyelles dans le mot/phrase", word)