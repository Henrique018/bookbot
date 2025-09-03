import sys

from stats import count_words
from stats import count_chars
from stats import sort_chars
 
def main():
    if (not sys.argv or len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    print('============ BOOKBOT ============')
    file_path = sys.argv[1]
    with open(file_path) as f:
        print(f'Analyzing book found at {file_path}...')
        file_contents = f.read()
        num_words = count_words(file_contents)
        chars_dict = count_chars(file_contents)
        sorted_dicts = sort_chars(chars_dict)
        
        print('----------- Word Count ----------')
        print(f'Found {num_words} total words')

        print('--------- Character Count -------')
        for dict in sorted_dicts:
            print(f"{dict['char']}: {dict['num']}")

        print('============= END ===============')

main()