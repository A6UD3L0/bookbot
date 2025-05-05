import sys

from stats import count_characters, count_words, create_report


def read_book(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content


def main(file_path):
    text_content = read_book(file_path)
    word_count = count_words(text_content)
    character_dict = count_characters(text_content)
    report = create_report(file_path, word_count, character_dict)
    print(report)


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

main(book_path)
