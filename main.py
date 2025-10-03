from stats import get_num_words, get_count_characters, sorting_dict
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        res = f.read()

    return res

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    num_words = get_num_words(content)
    character_counts = get_count_characters(content)
    character_counts = sorting_dict(character_counts)

    print("============ BOOKBOT ============")
    print(f" Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in character_counts.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")

main()