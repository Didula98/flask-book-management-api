# E/18/022
# AMARASINGHE D.I.
# Creating a REST Service with Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json() 
    
    # Validation checks
    if not new_book:
        return jsonify({"error": "No data provided"}), 400  # Bad Request if no data is provided
    
    if 'id' not in new_book or 'title' not in new_book or 'author' not in new_book:
        return jsonify({"error": "Missing required fields: id, title, author"}), 400  # Missing fields
    
    # Check if 'id' is unique
    if any(book['id'] == new_book['id'] for book in books):
        return jsonify({"error": "A book with this ID already exists"}), 400
    
    books.append(new_book)
    return jsonify(new_book), 201


# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book_data = request.get_json()  # Get the JSON data sent with the request

    # Find the book to update
    book = next((book for book in books if book['id'] == book_id), None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    # Check id 
    if 'id' in book_data and book_data['id'] != book_id:
        if any(existing_book['id'] == book_data['id'] for existing_book in books):
            return jsonify({"error": "A book with this ID already exists"}), 400

    # Update the book
    book.update(book_data)
    return jsonify(book)


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books = [book for book in books if book['id'] != book_id] # Remove the book from the list
        return jsonify({"message": "Book deleted"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)