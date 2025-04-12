#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Country, Learner, ProficiencyLevel, Card, Category

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        print("Clearing old data...")
        db.session.query(Learner).delete()
        db.session.query(ProficiencyLevel).delete()
        db.session.query(Card).delete()
        db.session.query(Category).delete()
        db.session.query(Country).delete()
        db.session.commit()

        print("Seeding countries...")
        countries= []
        country_names = ["China","Japan","Kenya","Madagascar","Botswana","Korea",]
        for name in country_names:
            country = Country(name=name)
            countries.append(country)
            db.session.add(country)

        db.session.commit()  

        print("Seeding user...")
        learners= []
        for _ in range(5):
             learner = Learner(
                  name = fake.name(), 
                  nickname=fake.first_name(),
                  country_id=rc(countries).id
                  )
             learners.append(learner)
             db.session.add(learner)

        db.session.commit()  

        print("Seeding categories...")
        categories=[]
        category_names = ["Greetings", "Directions", "Numbers", "Colors",  "Common Phrases"]
        for name in category_names:
            category = Category(name = name)
            categories.append(category)
            db.session.add(category) 

        db.session.commit()  
      

        print ("Seeding cards...")
        cards = []
        hsk_levels = ['HSK 1','HSK 2','HSK 3','HSK 4','HSK 5','HSK 6','HSK 7','HSK 8','HSK 9']
        hanzi_samples = [
            {"hanzi": "你好", "pinyin": "nǐ hǎo", "english": "Hello"},
            {"hanzi": "谢谢", "pinyin": "xiè xie", "english": "Thank you"},
            {"hanzi": "对不起", "pinyin": "duì bù qǐ", "english": "Sorry"},
            {"hanzi": "再见", "pinyin": "zài jiàn", "english": "Goodbye"},
            {"hanzi": "请", "pinyin": "qǐng", "english": "Please"}
        ]
        for _ in range(20):
             hanzi = rc(hanzi_samples)
             card = Card(
                  hanzi=hanzi['hanzi'],
                  pinyin=hanzi['pinyin'],
                  english_translation=hanzi['english'],
                  hsk_level=rc(hsk_levels),
                  category_id = rc (categories).id
             )
             db.session.add(card)
             cards.append(card)

        db.session.commit()  

          
        print("Seeding proficiency levels...")
        proficiency_levels = ["Beginner", "Intermediate", "Advanced"]
        for level in proficiency_levels:
             proficiency = ProficiencyLevel(
                  name =level,
                  description = fake.text(max_nb_chars = 100),
                  learner_id = rc (learners).id,
                  card_id = rc(cards).id
             )  
             db.session.add(proficiency)

        db.session.commit()   

                 

        print("Seed completed!")
