frank = "books/frankenstein.txt"
def get_book_text(path_file):
    with open(path_file) as f:
        file_content = f.read()
    return file_content

def word_count(path_file):
    word_count = len(get_book_text(path_file).split())
    return f"{word_count} words found in the document"

def main():
    print(word_count(frank))

main()