def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt", 'r') as f:
        file_contents = f.read()
        
    # Count and print word count
    wordcounter = word_count(file_contents)
    print(f"{wordcounter} words found in the document")

    # Count and sort characters
    character_counts = character_count(file_contents)
    character_list = character_counts.items()
    sorted_characters = sorted(character_list, key=lambda item: item[1], reverse=True)

    # Print character report
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")
        

def word_count(text):
    number_of_words = len(text.split())
    return number_of_words

def character_count(texts):
    lowercase = texts.lower()
    character = {}
    for text in lowercase:
        if text.isalpha():  # Ensure the character is alphabetical
            if text in character:
                character[text] += 1
            else:
                character[text] = 1
    return character

# Call the main function
main()