from stats import word_count, letter_count

def get_book_text(path_file):
    with open(path_file) as f:
        file_content = f.read()
    return file_content

def main():
    file_content = get_book_text("books/frankenstein.txt")
    Word_count = word_count(file_content)
    Letter_count = letter_count(file_content)
    print(Word_count)
    print(Letter_count)
main()