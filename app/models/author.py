from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates='author')

    def to_dict(self):
        author_dict = {
            "id": self.id,
            "name": self.name
        }
        author_dict["books"] = [book.title for book in self.books]

        return author_dict 

    def from_dict(cls, author_data):
        new_author = cls(
            name = author_data["name"]
        )
        return new_author

