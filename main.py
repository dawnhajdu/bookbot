from stats import count_text

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    
    return file_content

def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    return text
    
book_text = main()


num_words = count_text(book_text)
print(f"Found {num_words} total words")




    



