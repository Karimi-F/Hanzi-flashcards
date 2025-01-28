from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    nickname = db.Column(db.String, nullable = True)

    # One-to-many relationship with levels 
    levels = db.relationship('Level', back_populates = 'user', cascade = 'all, delete-orphan')

    def __repr__(self):
        return f'<User {self.id}, {self.name}, {self.nickname}>'

class Level(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationship with user
    user = db.relationship("User", back_populates = 'levels')

    # One-to-many relationship with cards
    cards = db.relationship('Card', back_populates = 'level', cascade = 'all, delete-orphan')

    def __repr__(self):
        return f'<Level {self.id}, with name {self.name} and description {self.description}, {self.user_id}'
    
class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key = True)
    hanzi = db.Column(db.String, nullable = False)
    pinyin =  db.Column(db.String, nullable = False)
    english_translation = db.Column(db.String, nullable = False)
    level_id = db.Column(db.Integer, db.ForeignKey ('levels.id'))

    # One-to-many relationship with levels
    level = db.relationship('Level', back_populates = 'cards')

    # Many-to-many relationship with categories
    card_categories = db.relationship("CardCategory", back_populates = "card", cascade = "all, delete-orphan")

    categories = association_proxy("card_categories", "category")

    serialize_rules = ("-card_categories.card",)

    def __repr__(self):
        return f'<Card with id{self.id}, Hanzi{self.hanzi}, Pinyin {self.pinyin}, English Translation {self.english_translation} is in level with id {self.level_id}>'
    
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String, nullable = False)
    description = db.Column (db.String, nullable = True)

    card_categories = db.relationship("CardCategory", back_populates = "category")

    serialize_rules = ("-card_categories.category",)

    def __repr__(self):
        return f'<Category with id {self.id} is called {self.name} and has the description {self.description}>'

class CardCategory(db.Model, SerializerMixin):
    __tablename__="card_categories"

    id = db.Column(db.Integer, primary_key = True)
    user_notes = db.Column(db.String, nullable = True)

    card_id = db.Column(db.Integer, db.ForeignKey('cards.id', ondelete = 'CASCADE'), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete = 'CASCADE'), nullable = False)


    card = db.relationship("Card", back_populates = "card_categories")
    category = db.relationship("Category", back_populates = "card_categories")

    serialize_rules = ("-card.card_categories", "-category.card_categories")

    def __repr__(self):
        return f'<Card category{self.user_notes}>'


