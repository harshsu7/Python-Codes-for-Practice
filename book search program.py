books = [
    "Five Point Someone",
    "The Alchemist",
    "To Kill a Mockingbird",
    "The Storm Before the Calm",
    "One Hundred Years of Solitude"
]

search = input("Enter book name to search: ").lower()

matches = []

for book in books:
    if search in book.lower():
        matches.append(book)

if matches:
    print("Books found:")
    for b in matches:
        print("-", b)
else:
    print("No book found")
