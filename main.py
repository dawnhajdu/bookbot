from stats import count_text, character_count, sort_items
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    
    return file_content

def main():
    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]

    text = get_book_text(filepath)
    return text
    
book_text = main()


num_words = count_text(book_text)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")

counting_characters = character_count(book_text)
#print(counting_characters)

new_dict = sort_items(counting_characters)
print("--------- Character Count -------")
for item in new_dict:
    if item["char"].isalpha():
        print(f"{item["char"]}: {item["num"]}")

#print([item["num"] for item in new_dict])
print("============= END ===============")
