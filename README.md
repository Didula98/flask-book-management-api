# flask-book-management-api
# Book Management API

## Description

This is a RESTful API for managing books, built with Flask and Docker. The API supports CRUD operations (Create, Read, Update, Delete) to manage a collection of books. It is designed to handle basic operations for adding, retrieving, updating, and deleting books, and is dockerized for easy deployment.

## Features

- **Create a Book**: Add a new book to the collection.
- **Retrieve Books**: Get a list of all books or retrieve a specific book by its ID.
- **Update a Book**: Modify the details of an existing book.
- **Delete a Book**: Remove a book from the collection.

## Installation

### Prerequisites

- Docker: Make sure Docker is installed on your machine. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Didula98/flask-book-management-api.git
   cd repository-name
2. **Build the Docker Image**
   ```bash
   docker build -t book-management-api .
4. **Run the Docker Container**
   ```bash
   docker run -d -p 5000:5000 book-management-api
6. **Access the API**
   The API will be available at http://localhost:5000 or http://127.0.0.1:5000.
