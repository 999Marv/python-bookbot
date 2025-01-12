def count_words(book):
    return len(book.split())

def count_chars(book):
    freq = {}
    for char in book:
        char = char.lower()
        if char.isalpha():
           freq[char] = freq.get(char, 0) + 1

    return freq

def aggregate_report(book):
    amount_of_words = count_words(book)
    char_frequency = count_chars(book)

    print(f"{amount_of_words} words found in the document")
    print(char_frequency)

def analyze_book(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        print(f"--- Begin report of {f.name} ---")
        aggregate_report(file_contents)
        print("--- End report ---") 
        
def main():
    analyze_book("books/frankenstein.txt")

main()