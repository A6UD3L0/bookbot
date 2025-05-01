
from stats import count_words, count_characters , create_report

def read_book(file_path): 
    with open(file_path) as f: 
        file_content= f.read()
        return file_content


def main(file_path): 
    text_content=read_book(file_path)
    print(text_content)
    word_count=count_words(text_content)
    print(word_count)
    character_dict=count_characters(text_content)
    print(character_dict)
    report=create_report(file_path, word_count, character_dict)
    print(report)

path_fr="books/frankenstein.txt"

main(path_fr)
