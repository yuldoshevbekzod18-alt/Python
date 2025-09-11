
import json

def read_student(file_path):
    try:
        with open(file_path,"r")as file:
            student=json.load(file)

            if isinstance(student,list):
                for idx,student in enumerate(student,start=1):
                    print(f"\nstudent{idx}:")
                    for key,value in student.items():
                        print(f"{key}:{value}")
            else:
                print("Error: JSON content is not a list of students.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in '{file_path}'.")

read_student('student.json') 

#Task: Movie Recommendation System
#Use this url http://www.omdbapi.com/ to fetch information about movies.
#Create a program that asks users for a movie genre and recommends a random movie from that genre.
import requests
import random

# Replace this with your actual OMDb API key
OMDB_API_KEY = "your_api_key_here"
OMDB_URL = "http://www.omdbapi.com/"

GENRE_MOVIES = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "comedy": ["The Grand Budapest Hotel", "Superbad", "Step Brothers"],
    "drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club"],
    "sci-fi": ["Inception", "The Matrix", "Interstellar"],
    "horror": ["The Conjuring", "Get Out", "A Quiet Place"]
}

def get_movie_info(title):
    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }
    response = requests.get(OMDB_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            print("Movie not found:", data.get("Error"))
    else:
        print("API request failed.")
    return None

def recommend_movie(genre):
    genre = genre.lower()
    if genre not in GENRE_MOVIES:
        print("Sorry, genre not available. Choose from:", ", ".join(GENRE_MOVIES.keys()))
        return

    movie_title = random.choice(GENRE_MOVIES[genre])
    movie_info = get_movie_info(movie_title)

    if movie_info:
        print("\n🎬 Movie Recommendation:")
        print("Title:      ", movie_info.get("Title"))
        print("Year:       ", movie_info.get("Year"))
        print("Genre:      ", movie_info.get("Genre"))
        print("Plot:       ", movie_info.get("Plot"))
        print("IMDb Rating:", movie_info.get("imdbRating"))

def main():
    print("🎥 Welcome to the Movie Recommendation System!")
    genre = input("Enter a genre (action, comedy, drama, sci-fi, horror): ")
    recommend_movie(genre)

if __name__ == "__main__":
    main()

#Task: JSON Modification
#Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
# book json
[
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": "1937"
    }
]

import json
import os

BOOKS_FILE = 'books.json'

def load_books():
    """Load books from the JSON file."""
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    """Save books to the JSON file."""
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def add_book():
    """Add a new book."""
    books = load_books()
    new_id = max([book['id'] for book in books], default=0) + 1
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    new_book = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year
    }
    books.append(new_book)
    save_books(books)
    print("✅ Book added successfully!")

def update_book():
    """Update an existing book."""
    books = load_books()
    book_id = int(input("Enter the ID of the book to update: "))
    for book in books:
        if book['id'] == book_id:
            book['title'] = input(f"Enter new title [{book['title']}]: ") or book['title']
            book['author'] = input(f"Enter new author [{book['author']}]: ") or book['author']
            book['year'] = input(f"Enter new year [{book['year']}]: ") or book['year']
            save_books(books)
            print("✅ Book updated successfully!")
            return
    print("❌ Book not found.")

def delete_book():
    """Delete a book."""
    books = load_books()
    book_id = int(input("Enter the ID of the book to delete: "))
    new_books = [book for book in books if book['id'] != book_id]
    if len(books) == len(new_books):
        print("❌ Book not found.")
    else:
        save_books(new_books)
        print("✅ Book deleted successfully!")

def list_books():
    """List all books."""
    books = load_books()
    if not books:
        print("📭 No books found.")
        return
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")

def main():
    """Main menu."""
    while True:
        print("\n📘 Book Manager")
        print("1. List all books")
        print("2. Add a new book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            list_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
