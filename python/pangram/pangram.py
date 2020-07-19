def is_pangram(sentence):
    alphabet = "abcdefghigklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True
