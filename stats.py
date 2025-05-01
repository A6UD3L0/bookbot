def count_words(text_content): 
    word_count=len(text_content.split(" "))
    return word_count 

def count_characters(text_content): 
    text_content_lower=text_content.lower()
    character_dict={}
    for char in text_content_lower: 
        if char in character_dict.keys(): 
            character_dict[char] += 1
        else:  
            character_dict[char] = 1
    return character_dict

def create_report(book_path,word_count,character_dict):
    character_dict_sorted=character_dict.sort(reverse=True, key=sort_on)
    nice_word_count=f"Found {word_count} total words" 
    report= book_path + nice_word_count + character_dict_sorted
    return report 
    
