def word_count(file):
    word_count = len(file.split())
    return f"Found {word_count} total words"

def letter_count(File):
    file = File.lower()
    letter_count = {}
    for i in file:
        if i not in letter_count:
            letter_count[i]=0
    for i in file:
        letter_count[i] += 1
    return letter_count

def sort_on(items):
    return items["num"]

def letter_sort(dic):
    letters = []
    for letter in dic:
        if letter.isalpha():
            char = {}
            char["char"] = letter
            char["num"] = dic[letter]
            letters.append(char)
    letters.sort(reverse=True, key=sort_on)
    return letters
