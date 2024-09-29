book_path = "books/frankenstein.txt"

with open('books/frankenstein.txt', 'r') as file:
    content = file.read()
    print(content)

def count_words(book):
    words = book.split()
    return f"{len(words)} words found in the document"

def count_characters(book):
    count = {}
    for i in book:
        char = i.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
    


num_words = count_words(content)
message = count_characters(content)
print(message)
print()

print(f"--- Begin report of {book_path} ---")
print()
print(f"{num_words} words found in the document")
print()

def obter_quantidade(item):
    return item[1]


relatorio = sorted(message.items(), key=obter_quantidade, reverse=True)


for k, v in relatorio:
    if k.isalpha()== True:
        print(f"The '{k}' character was found {v} times")

print()
print("--- End report ---")