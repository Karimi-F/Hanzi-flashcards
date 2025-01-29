#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import Country, Learner, ProficiencyLevel, Card, Category
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class CardList(Resource):
    def get(self):
        cards = Card.query.all()
        card_list = [
            {"id": card.id, 
             "hanzi": card.hanzi, 
             "pinyin": card.pinyin, 
             "english_translation": card.english_translation, 
             "hsk_level":card.hsk_level,
             "category_id" : card.category.id
             } 
             for card in cards
        ]

        if cards:
            response_body = card_list
            response_status = 200

        else:
            response_body = {"error": "No cards found."}
            response_status = 404

        response = make_response(jsonify(response_body), response_status)
        return response
    
    def post(self):
        data = request.get_json()
        hanzi = data.get("hanzi")
        pinyin = data.get("pinyin")
        english_translation = data.get("english_translation")
        hsk_level = data.get("hsk_level")
        category_id = data.get("category_id")

        if not hanzi or not pinyin or not english_translation or hsk_level or category_id is None:
            return {"error": "Missing required fields: hanzi, pinyin, english_translation or level_id."},400
        
        category = Category.query.get(category_id)
        if not category:
            return {"error":f"Category with category ID {category_id} not found."},404
        
        new_card = Card(
            hanzi=hanzi,
            pinyin=pinyin,
            english_translation=english_translation,
            hsk_level=hsk_level,
            category_id=category_id
        )
        db.session.add(new_card)
        db.session.commit()

        response_body = {
            "hanzi":new_card.hanzi,
            "pinyin":new_card.pinyin,
            "english_translation":new_card.english_translation,
            "hsk_level":new_card.hsk_level,
            "category_id":new_card.category_id
        }
        return response_body,201
    
api.add_resource(CardList, '/cards', methods = ['GET', 'POST'])

# class CardById(Resource):
#     def get(self, id):
#         card = Card.query.get(id)

#         if card:
#             response_body = {
#                 "id": card.id,
#                 "hanzi":card.hanzi,
#                 "pinyin":card.pinyin,
#                 "english_translation":card.english_translation,
#                 "level_id":card.level.id
#             }
#             response_status = 200

#         else:
#             response_body = {"error":f"Card with ID {id} not found."}
#             response_status = 404

#         return make_response(jsonify(response_body), response_status)

#     def patch(self,id):
#         card = Card.query.get(id)

#         if not card:
#             return {"error":f"Card with id {id} not found."},404    
        
#         else:
#             data = request.get_json()    

#             if "hanzi" in data:
#                 card.hanzi = data["hanzi"]

#             if "pinyin" in data:
#                 card.pinyin = data["pinyin"]

#             if "english_translation" in data:
#                 card.english_translation = data["english_translation"]

#             if "level_id" in data:
#                 level = Level.query.get(data["level_id"])
#                 if not level:
#                     return {"error":f"Level with ID {data['level_id']} not found."}, 404
#                 card.level_id = data["level_id"]

#         db.session.commit()    

#         response_body = {
#             "id" : card.id,
#             "hanzi" : card.hanzi,
#             "pinyin" : card.pinyin,
#             "english_translation" : card.english_translation,
#             "level_id" : card.level_id 
#         }
#         return make_response(jsonify(response_body), 200)

#     def delete(self,id):
#         card = Card.query.get(id)

#         if card:
#             db.session.delete(card)
#             db.session.commit()

#             response_body = {"message":f"Card with ID {id} has been deleted successfully."}
#             response_status = 200

#         else:
#             response_body = {"error":f"Card with ID {id} not found."}
#             response_status = 404

#         return make_response(jsonify(response_body), response_status)        

# api.add_resource(CardById, '/card/<int:id>')        


# class UserList(Resource):
#     def get(self):
#         users = User.query.all()
#         user_list = [
#             {
#                 "id": user.id,
#                 "name": user.name,
#                 "nickname": user.nickname
#             } 
#             for user in users
#         ]
#         if users:
#             response_body = user_list
#             response_status = 200
#         else:
#             response_body = {"error": "Users not found"} 
#             response_status = 404
#         response =  make_response(jsonify(response_body),response_status)
#         return response
    
#     def post(self):
#         data = request.get_json()
#         name = data.get("name")
#         nickname = data.get("nickname")

#         if name is None or nickname is None:
#             return {"error":"Missing required fields. Either name or nickname."},404
        
#         else:
#             new_user = User(
#                 name = name,
#                 nickname = nickname
#             )
#             db.session.add(new_user)
#             db.session.commit()

#             response_body = {
#                 "id" : new_user.id,
#                 "name" : new_user.name,
#                 "nickname" : new_user.nickname
#             }
#             response_status = 201
#             response = make_response(jsonify(response_body),response_status)

#             return response
   
# api.add_resource(UserList, '/users')    

# class UserByID(Resource):
#     def get(self, id):
#         user = User.query.get(id)

#         if user:
#             response_body = {
#                 "id": user.id,
#                 "name":user.name,
#                 "nickname":user.nickname
#             }
#             response_status = 200

#         else:
#             response_body = {"error" : f"User with ID {id} not found."}
#             response_status = 404

#         return make_response(jsonify(response_body), response_status)    

# api.add_resource(UserByID, '/user/<int:id>')


# class LevelList(Resource):
#     def get(self):
#         levels = Level.query.all()
#         level_list = [
#             {"id":level.id,
#             "name":level.name,
#             "description": level.description,
#             "user_id":level.user_id
#             } for level in levels
#         ]
#         if levels:
#             response_body = level_list
#             response_status = 200
#         else:
#             response_body = {"error":"Levels not found"}
#             response_status = 404
#         response = make_response(jsonify(response_body),response_status)
#         return response        
        
#     def post(self):
#         data = request.get_json()
#         name = data.get("name")
#         description = data.get("description")
#         user_id = data.get("user_id")

#         if name is None or description is None or user_id is None:
#             return {"error":"Missing required fields. Either name, description or user_id."},404
        
#         else:
#             new_level = Level(
#                 name = name,
#                 description = description,
#                 user_id = user_id
#             )
#             db.session.add(new_level)
#             db.session.commit()

#             response_body = {
#                 "id" :new_level.id,
#                 "name":new_level.name,
#                 "description":new_level.description,
#                 "user_id":new_level.user_id
#             }
#             response_status = 201
#             response = make_response(jsonify(response_body), response_status)
#             return response

# api.add_resource(LevelList, '/levels')        

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# # GET ALL Cards /cards DONE
# # POST Card /cards DONE
# # GET Card by id /card/id DONE
# # PATCH Card card/id DONE
# # DELETE Card card/id DONE

# # GET all Users /users DONE
# # POST User /users DONE
# # GET User by id /user/id DONE

# # GET all Levels /levels DONE
# # POST Level /levels DONE
# # GET Level by id /level/id

# # GET all Categories /categories
# # POST Category /categories
# # GET Category by id /categories/id