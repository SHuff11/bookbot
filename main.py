import sys
from stats import word_count, character_count, sort_dict

def main():
    print("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = word_count(text)
    char_count = character_count(text)
    sorted_dict = sort_dict(char_count)  
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {path}... \n----------- Word Count ---------- \nFound {num_words} total words \n--------- Character Count -------")
    for x in sorted_dict:
        if x['char'].isalpha():
            print(f"{x['char']}: {x['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

main()