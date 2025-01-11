def main():
    with open("/Users/heathhile/workspace/github.com/heathhile/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = (count_words(file_contents))
    chars_dict = (count_chars(file_contents.lower()))
    report = make_report(chars_dict, num_words)

def count_words(words):
    return len(words.split())

def count_chars(the_chars):
    chars = {}
    for char in the_chars:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def make_report(more_chars, words):
    item_list = list(more_chars.items())
    sorted_list = sorted(item_list, key=lambda item:item[1], reverse=True)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()
    for char, num in sorted_list:
        if char.isalpha():
            print(f"The '{char}' character was found '{num}' times ")
    print("--- End report ---")



main()