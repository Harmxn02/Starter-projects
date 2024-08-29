def pig_latin(string: str) -> str:
    # Vowels list
    lst_vowels = ["a", "e", "i", "o", "u"]

    # If the word starts with a vowel
    if string[0].lower() in lst_vowels:
        return string + "way"

    # If the word starts with a consonant or consonant cluster
    get_all_letters_until_vowel = []

    for char in string:
        if char.lower() not in lst_vowels:
            get_all_letters_until_vowel.append(char)
        else:
            break

    # Converting the list to a string
    first_consonant_cluster = "".join(get_all_letters_until_vowel)

    # Get the rest of the string after the first consonant cluster
    rest_of_word = string[len(first_consonant_cluster) :]

    # Form the Pig Latin word
    pig_latin_word = rest_of_word + first_consonant_cluster + "ay"

    return pig_latin_word


# Test the function
if __name__ == "__main__":
    print("🟩 Test case 'pig'" if pig_latin("pig") == "igpay" else "🟥 Test case 'pig'")
    print("🟩 Test case 'latin'" if pig_latin("latin") == "atinlay" else "🟥 Test case 'latin'")
    print("🟩 Test case 'banana'" if pig_latin("banana") == "ananabay" else "🟥 Test case 'banana'")
    print("🟩 Test case 'friends'" if pig_latin("friends") == "iendsfray" else "🟥 Test case 'friends'")
    print("🟩 Test case 'smile'" if pig_latin("smile") == "ilesmay" else "🟥 Test case 'smile'")
    print("🟩 Test case 'string'" if pig_latin("string") == "ingstray" else "🟥 Test case 'string'")
    print("🟩 Test case 'eat'" if pig_latin("eat") == "eatway" else "🟥 Test case 'eat'")
    print("🟩 Test case 'omelet'" if pig_latin("omelet") == "omeletway" else "🟥 Test case 'omelet'")