# stats.py


def count_words(text_content):
    return len(text_content.split())


def count_characters(text_content):
    text_content_lower = text_content.lower()
    character_dict = {}
    for char in text_content_lower:
        if char in character_dict.keys():
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict


def create_report(book_path, word_count, character_dict):
    report = (
        "----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        "--------- Character Count -------\n"
    )

    sorted_chars = sorted(
        character_dict.items(), key=lambda item: item[1], reverse=True
    )
    for char, count in sorted_chars:
        report += f"{char}: {count}\n"

    return report
