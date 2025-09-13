from stats import get_word_count, get_char_count, get_sorted_char_count
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_counts = get_char_count(text)
    sorted_chars = get_sorted_char_count(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["num"]
        
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()