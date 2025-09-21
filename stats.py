def word_count(file):
    word_count = len(file.split())
    return f"{word_count} words found in the document"

def letter_count(file):
    letter_count = {}
    for i in file:
        if i not in letter_count:
            letter_count[i]=0
    for i in file:
        letter_count[i] += 1
    return letter_count