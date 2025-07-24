def get_num_words(book_text):
    book_words = book_text.split()
    num_words = len(book_words)
    return num_words
        

def get_num_chars(book_text):
    char_counts = {}
    for char in book_text:
        c = char.lower()
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts


def create_report(book_text):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    total_words = get_num_words(book_text)
    character_counts = get_num_chars(book_text)
    
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for ch, count in sorted(character_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{ch}: {count}")
    print("============= END ===============")