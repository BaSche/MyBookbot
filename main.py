from collections import Counter


def main():
    path = "books/frankenstein.txt"
    content = read_book(path)
    words = count_words(content)
    # print(count_chars(content))
    filtered = filter_chars_for_alpha(count_chars(content))
    sorted_chars = dict(sorted(filtered.items(), key=lambda pair: pair[1],reverse=True))
    report(path, words, sorted_chars)

def report(path, words, char_counter):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for char in char_counter:
        print(f"The '{char}' character was found {char_counter[char]} times")

def read_book(path):
    with open(path) as book:
        content = book.read()
        return content

def count_words(text):
    return len(text.split())

def count_chars(text):
    counter=Counter(text.lower())
    return counter

def filter_chars_for_alpha (counter):
    return dict(filter(lambda pair: pair[0].isalpha() , counter.items()))


main()
