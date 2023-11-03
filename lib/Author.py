import sqlite3

CONN = sqlite3.connect('Magazine.db')
CURSOR = CONN.cursor()

class Author:
    def __init__(self, name):
        self.name = name

    def author_name(self):
        return self.name
    
    def articles(self):
        return [article for article in Article.all_articles() if article.author() == self]
    
    def magazines(self):
        return list(set([magazine for magazine in Magazine.all_magazines() if self in magazine.authors()]))
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self, magazine):
        return list(set([magazine.category() for magazine in self.magazines()]))

    @classmethod
    def all_authors(cls):
        return cls.all_authors

    @classmethod
    def create_author_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS Authors(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )''')
        CONN.commit()

    def save_author(self):
        CURSOR.execute('INSERT INTO Authors (name) VALUES (?)', (self.name,))
        CONN.commit()
        

    @classmethod
    def create_author(cls, name):
        author = cls(name)
        author.save_author()
        return author

Author.create_author_table()

author1 = Author.create_author("John Doe")
author2 = Author.create_author("Jane Smith")       


CONN.commit()

    