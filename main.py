def read_book(file_path): 
    with open(file_path) as f: 
        file_content= f.read()
        return file_content

def main(file_path): 
    text_content=read_book(file_path)
    print(text_content)



path_fr="books/frankenstein.txt"

main(path_fr)
