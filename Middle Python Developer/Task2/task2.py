import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the 'books' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        published_year INTEGER NOT NULL
    )
''')
conn.commit()

def add_book(title, author, published_year):
    cursor.execute('''
        INSERT INTO books (title, author, published_year) 
        VALUES (?, ?, ?)
    ''', (title, author, published_year))
    conn.commit()
    print(f"Added book: {title} by {author} ({published_year})")

def get_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    return books

def update_book(book_id, title, author, published_year):
    cursor.execute('''
        UPDATE books
        SET title=?, author=?, published_year=?
        WHERE id=?
    ''', (title, author, published_year, book_id))
    conn.commit()
    print(f"Updated book with ID {book_id}")

def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    conn.commit()
    print(f"Deleted book with ID {book_id}")

# Example usage:
add_book("The Catcher in the Rye", "J.D. Salinger", 1951)
add_book("To Kill a Mockingbird", "Harper Lee", 1960)

print("All books:")
print(get_books())

update_book(1, "The Catcher in the Rye", "Jerome David Salinger", 1951)

print("After update:")
print(get_books())

delete_book(2)

print("After deletion:")
print(get_books())

# Close the database connection when done
conn.close()
