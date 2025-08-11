from stats import get_word_count, get_book_text, character_count, character_sorting
import sys
def main():
    path = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_word_count(text)
    count = character_count(text)
    sorted_letters = character_sorting(count)
    print_report(path, num_words , sorted_letters)


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
if __name__ == "__main__":
    main()