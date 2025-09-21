from stats import word_count, letter_count, letter_sort

def get_book_text(path_file):
    with open(path_file) as f:
        file_content = f.read()
    return file_content

def main():
    file_content = get_book_text("books/frankenstein.txt")
    Word_count = word_count(file_content)
    Letter_count = letter_count(file_content)
    sorted_letter = letter_sort(Letter_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(Word_count)
    print("--------- Character Count -------")
    
    for letter in sorted_letter:
        print(f"{letter["char"]}: {letter["num"]}")

    print("============= END ===============")

    
main()