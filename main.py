from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as file:
        f_contents = file.read()
    return f_contents



def main():
    contents = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(contents)
    print(f"{num_words} words found in the document")

main()