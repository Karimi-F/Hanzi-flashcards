from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Country(db.Model, SerializerMixin):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    # # One-to-many relationship with learners 
    learners = db.relationship('Learner', back_populates = 'country', cascade = 'all, delete-orphan')

    serialize_rules = ("-learners.country",)

    def __repr__(self):
        return f'<Country: {self.id}, {self.name}>'
    
class Learner(db.Model, SerializerMixin):
    __tablename__ = 'learners'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    nickname = db.Column(db.String, nullable = True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    proficiencylevels = db.relationship('ProficiencyLevel', back_populates = 'learner', cascade ='all, delete-orphan')

    cards = association_proxy('proficiencylevels', 'card')

    country = db.relationship('Country', back_populates = 'learners')

    serialize_rules = ("-country.learners", "-proficiencylevels.learner")

    def __repr__(self):
        return f'<Learner {self.id}, {self.name}, {self.nickname} from country with id {self.country_id}>'
    

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key = True)
    hanzi = db.Column(db.String, nullable = False)
    pinyin =  db.Column(db.String, nullable = False)
    english_translation = db.Column(db.String, nullable = False)
    hsk_level = db.Column(db.String, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id", ondelete="CASCADE"))

    proficiencylevels = db.relationship('ProficiencyLevel', back_populates = 'card', cascade='all, delete-orphan')

    category = db.relationship('Category', back_populates='cards')

    serialize_rules = ("-proficiencylevels.card", "-category.cards")

    def __repr__(self):
        return f'<Card with id{self.id}, Hanzi{self.hanzi}, Pinyin {self.pinyin}, English Translation {self.english_translation} and is in HSK Level {self.hsk_level} is in the category with id {self.category_id}>'


class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False) 

    cards = db.relationship('Card', back_populates='category', cascade = 'all, delete-orphan')

    serialize_rules = ("-cards.category",)

    def __repr__(self):
        return f'Category with id {self.id} is called {self.name}'       

class ProficiencyLevel(db.Model):
    __tablename__ = 'proficiencylevels'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)

    learner_id = db.Column(db.Integer, db.ForeignKey('learners.id', ondelete = "CASCADE"), nullable = False)
    card_id = db.Column(db.Integer, db.ForeignKey("cards.id", ondelete = "CASCADE"), nullable=False)

    learner = db.relationship('Learner', back_populates='proficiencylevels')
    card = db.relationship('Card', back_populates = 'proficiencylevels')

    serialize_rules = ("-learner.proficiencylevels", "-card.proficiencylevels")


    def __repr__(self):
        return f'<Proficiency Level with name {self.name} and description {self.description}:Learner {self.learner_id}, Card {self.card_id}>'

