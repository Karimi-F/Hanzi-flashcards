from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    nickname = db.Column(db.String, nullable = True)

    def __repr__(self):
        return f'<User {self.id}, {self.name}, {self.nickname}>'


class Level(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Level {self.id}, with name {self.name} and description {self.description}, {self.userid}'
    
class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key = True)
    hanzi = db.Column(db.String, nullable = False)
    pinyin =  db.Column(db.String, nullable = False)
    english_translation = db.Column(db.String, nullable = False)
    level_id = db.Column(db.Integer, db.ForeignKey ('levels.id'))

    def __repr__(self):
        return f'<Card with id{self.id}, Hanzi{self.hanzi}, Pinyin {self.pinyin}, English Translation {self.english_translation} is in level with id {self.level_id}>'
    
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String, nullable = False)
    description = db.Column (db.String, nullable = True)

    def __repr__(self):
        return f'<Category with id {self.id} is called {self.name} and has the description {self.description}>'
    
