import sys

from stats import count_words
from stats import count_characters
from stats import get_sorted_count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    text = get_book_text(path)
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    character_count = count_characters(text)
    sorted_characters = get_sorted_count_characters(character_count)
    print("--------- Character Count -------")
    for dict in sorted_characters:
        char = list(dict.keys())[0]
        if char.isalpha():
            print(f"{char}: {dict[char]}")

main()
