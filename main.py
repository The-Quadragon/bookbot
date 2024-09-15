def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_count(text)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_count(text):
    counts = {}
    words = text.split()
    for w in words:
        lowered = w.lower()
        for c in lowered:
            if c is counts[c]:
                counts[c] += 1
            else:
                counts[c] = 1
    for value in counts:
        print(value)
    #return counts

main()
