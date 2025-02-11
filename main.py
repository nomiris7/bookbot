FILEPATH = "books/frankenstain.txt"

def count_symbols(text):
    letters = {}
    for letter in text.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def count_words(text):
    sum = 0
    for word in text.split():
        sum += 1
    return sum

def create_raport(num_words: int, symbols: dict):
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    list_of_dict = []
    for letter in symbols:
        if letter in alphabet:
            list_of_dict.append({"letter":  letter,
                                 "num_of_occurrence": symbols[letter]})
    print(f"--- Begin report of {FILEPATH} ---")
    print(f"{num_words} found in the document")
    list_of_dict.sort(reverse=True,key=lambda d : d["num_of_occurrence"])
    for letter in list_of_dict:
        print(f"The '{letter['letter']}' character was found {letter['num_of_occurrence']} times")
    print("--- End report ---")



with open(FILEPATH) as file:
    file_contents = file.read()
    word_count = count_words(file_contents)
    symbols_count = count_symbols(file_contents)
    create_raport(word_count, symbols_count)