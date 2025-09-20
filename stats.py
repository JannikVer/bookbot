def word_count(path_file):
    with open(path_file) as f:
        file_content = f.read()
    word_count = len(file_content.split())
    return f"{word_count} words found in the document"

def letter_count(path_file):
    with open(path_file) as f:
        file_content = list(f.read().lower())
    letter_count = {}
    for i in file_content:
        if i not in letter_count:
            letter_count[i]=0
    for i in file_content:
        letter_count[i] += 1
    return letter_count