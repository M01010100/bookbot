def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words=text.split()
    return len(words)

def main():
    output = get_book_text("books/frankenstein.txt")
    print(f"{get_word_count(output)} words found in the document")

main()