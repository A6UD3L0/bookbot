
from stats import count_words, count_characters  


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


path_fr="books/frankenstein.txt"

main(path_fr)
