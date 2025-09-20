def word_count(path_file):
    with open(path_file) as f:
        file_content = f.read()
    word_count = len(file_content.split())
    return f"{word_count} words found in the document"