def get_word_count(text):
    words=text.split()
    return len(words)

def get_char_count(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_char_count(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list