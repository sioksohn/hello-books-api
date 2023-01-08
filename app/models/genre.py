from app import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

def to_dict(self):
    genre_dict = {
        "id" : self.id,
        "name": self.name
    }

    return genre_dict

def from_dict(cls, genre_data):
    new_genre = cls(
        name = genre_data["name"]
    )

    return new_genre