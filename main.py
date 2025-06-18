import sys
from stats import count_words, count_chars, sort_char_counts

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at '{filepath}' does not exist.")
    except Exception as e:
        print(f"An error occured: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)
    if not book_text:
        print("Failed to load book.")
        return
    
    word_count = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")

    char_count = count_chars(book_text)
    sorted_count = sort_char_counts(char_count)

    print("--------- Character Count -------")
    for sc in sorted_count:
        print(f"{sc['char']}: {sc['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()