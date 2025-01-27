#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Level, Card, Category

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        print("Clearing old data...")
        db.session.query(User).delete()
        db.session.query(Level).delete()
        db.session.query(Card).delete()
        db.session.query(Category).delete()
        db.session.commit()

        print("Seeding user...")
        users = []
        for _ in range(5):
             user = User(
                  name = fake.name(), 
                  nickname=fake.first_name()
                  )
             users.append(user)
             db.session.add(user)

        db.session.commit()  
        
        print("Seeding levels...")
        levels = []
        for _ in range (10):
             level = Level(
                  name = f"Level {randint(1, 10)}",
                  description = fake.text(max_nb_chars = 100),
                  user_id = rc (users).id
             )  
             levels.append(level)
             db.session.add(level)

        db.session.commit()   

        print ("Seeding cards...")
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
                  level_id = rc (levels).id
             )
             db.session.add(card)

        db.session.commit()  

        print("Seeding categories...")
        categories=[]
        category_names = ["Beginner","Intermediate", "Advanced", "Greetings", "Directions"]
        for name in category_names:
            category = Category(name = name, description=fake.text(max_nb_chars=100))
            categories.append(category)
            db.session.add(category) 

        db.session.commit()            

        print("Seed completed!")
