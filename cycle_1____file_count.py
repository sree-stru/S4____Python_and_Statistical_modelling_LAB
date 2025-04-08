import string

def count_file_contents(filename):
    word_count = 0
    sentence_count = 0
    uppercase_count = 0
    lowercase_count = 0
    special_char_count = 0

    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            sentence_count = sum(1 for char in text if char in '.!?')
            for char in text:
                if char.isupper():
                    uppercase_count += 1
                elif char.islower():
                    lowercase_count += 1
                elif char in string.punctuation:
                    special_char_count += 1

        print(f"Word count: {word_count}")
        print(f"Sentence count: {sentence_count}")
        print(f"Uppercase letters: {uppercase_count}")
        print(f"Lowercase letters: {lowercase_count}")
        print(f"Special characters: {special_char_count}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = 'fileinput.txt'
count_file_contents(filename)
