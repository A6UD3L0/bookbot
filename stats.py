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


