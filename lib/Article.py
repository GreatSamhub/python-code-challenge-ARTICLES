import sqlite3
from Author import Author
from Magazine import Magazine
CONN = sqlite3.connect('Magazine.db')
CURSOR = CONN.cursor()

class Article:
    all_articles = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    def author(self):
        return self.author
    
    def magazine(self):
        return self.magazine
    
    def title(self):
        return self.title
    
    def article_author(self):
        return self.author
    
    def article_magazine(self):
        return self.magazine
    
    @classmethod
    def create_article_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS Articles(
            id INTEGER PRIMARY KEY,
            author_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            author TEXT NOT NULL,
            magazine TEXT NOT NULL,
            title TEXT NOT NULL
        )''')
        CONN.commit()

    def save_article(self):
        CURSOR.execute('INSERT INTO Articles (author_id, magazine_id, author, magazine, title) VALUES (?, ?, ?, ?, ?)', (self.author.id, self.magazine.id, self.author.name, self.magazine.name, self.title))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create_article(cls, author, magazine, title):
        article = cls(author, magazine, title)
        article.save_article()
        return article
    

