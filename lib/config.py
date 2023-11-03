import sqlite3
from Author import Author
from Magazine import Magazine

CONN = sqlite3.connect('Magazine.db')
CURSOR = CONN.cursor()

class Author:
    def __init__(self, name):
        self.name = name

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

def create_tables():
    CURSOR.execute('''CREATE TABLE IF NOT EXISTS Authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )''')

    CURSOR.execute('''CREATE TABLE IF NOT EXISTS Magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )''')

    CURSOR.execute('''CREATE TABLE IF NOT EXISTS Articles (
        id INTEGER PRIMARY KEY,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        FOREIGN KEY (author_id) REFERENCES Authors (id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines (id)
    )''')

    CONN.commit()

def save_data():
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Magazine", "Technology")
    magazine2 = Magazine("Sports News", "Sports")

    article1 = Article(author1, magazine1, "Tech Trends")
    article2 = Article(author2, magazine1, "New Gadgets")
    article3 = Article(author2, magazine2, "World Cup Recap")

    CONN.commit()

create_tables()
save_data()

CONN.close()
