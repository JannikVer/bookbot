from stats import word_count

frank = "books/frankenstein.txt"
def get_book_text(path_file):
    with open(path_file) as f:
        file_content = f.read()
    return file_content

def main():
    print(word_count(frank))

main()