books = [("The Great Gatsby", "F. Scott Fitzgerald"), 
         ("To Kill a Mockingbird", "Harper Lee"), 
         ("1984", "George Orwell"), 
         ("Pride and Prejudice", "Jane Austen")]

sorted_books = sorted(books, key=lambda x: x[1])

print(sorted_books)
