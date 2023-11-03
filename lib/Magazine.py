import sqlite3

CONN = sqlite3.connect('Magazine.db')
CURSOR = CONN.cursor()

class Magazine:
    all_magazines = []
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    def magazine_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def category(self):
        return self._category

    def set_category(self, category):
        self._category = category
    
    @classmethod
    def magazine_all(cls):
        return cls.all_magazines

    def magazine_contributors(self):
        return [author for author in Author.all_authors() if self in author.magazines()]
    
    @classmethod
    def magazine_find_by_name(cls, name):
        return [magazine for magazine in Magazine.all_magazines() if magazine.magazine_name() == name]

    @classmethod
    def magazine_article_titles(cls):
        return [article.title for article in Article.all_articles() if article.magazine() == cls]

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS Magazines(
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            category TEXT NOT NULL
        )''')
        CONN.commit()

    def save_magazine(self):
        CURSOR.execute('INSERT INTO Magazines(name, category) VALUES (?, ?)', (self._name, self._category))
        CONN.commit()

    @classmethod
    def create_magazine(cls, magazine_name, magazine_category):
        magazine = cls(magazine_name, magazine_category)
        magazine.save_magazine()
        return magazine

Magazine.create_table()

magazine1 = Magazine.create_magazine("Tech Magazine", "Technology")
magazine2 = Magazine.create_magazine("Sports News", "Sports")

CONN.commit()
