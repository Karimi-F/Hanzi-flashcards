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

        if not hanzi or not pinyin or not english_translation or hsk_level is None or category_id is None:
            return {"error": "Missing required fields: hanzi, pinyin, English Translation, hsk Level or category id."},400
        
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

class CardById(Resource):
    def get(self, id):
        card = Card.query.get(id)

        if card:
            response_body = {
                "id": card.id,
                "hanzi":card.hanzi,
                "pinyin":card.pinyin,
                "english_translation":card.english_translation,
                "hsk_level":card.hsk_level,
                "category_id":card.category.id
            }
            response_status = 200

        else:
            response_body = {"error":f"Card with ID {id} not found."}
            response_status = 404

        return make_response(jsonify(response_body), response_status)

    def patch(self,id):
        card = Card.query.get(id)

        if not card:
            return {"error":f"Card with id {id} not found."},404    
        
        else:
            data = request.get_json()    

            if "hanzi" in data:
                card.hanzi = data["hanzi"]

            if "pinyin" in data:
                card.pinyin = data["pinyin"]

            if "english_translation" in data:
                card.english_translation = data["english_translation"]

            if "hsk_level" in data:
                card.hsk_level = data["hsk_level"]    

            if "category_id" in data:
                category = Category.query.get(data["category_id"])
                if not category:
                    return {"error":f"Category with ID {data['category_id']} not found."}, 404
                card.category_id = data["category_id"]

        db.session.commit()    

        response_body = {
            "id" : card.id,
            "hanzi" : card.hanzi,
            "pinyin" : card.pinyin,
            "english_translation" : card.english_translation,
            "hsk_level":card.hsk_level,
            "category_id" : card.category_id 
        }
        return make_response(jsonify(response_body), 200)

    def delete(self,id):
        card = Card.query.get(id)

        if card:
            db.session.delete(card)
            db.session.commit()

            response_body = {"message":f"Card with ID {id} has been deleted successfully."}
            response_status = 200

        else:
            response_body = {"error":f"Card with ID {id} not found."}
            response_status = 404

        return make_response(jsonify(response_body), response_status)        

api.add_resource(CardById, '/card/<int:id>')        


class LearnerList(Resource):
    def get(self):
        learners = Learner.query.all()
        learner_list = [
            {
                "id": learner.id,
                "name": learner.name,
                "nickname": learner.nickname,
                "country_id":learner.country_id
            } 
            for learner in learners
        ]
        if learners:
            response_body = learner_list
            response_status = 200
        else:
            response_body = {"error": "Learners not found"} 
            response_status = 404
        response =  make_response(jsonify(response_body),response_status)
        return response
    
    def post(self):
        data = request.get_json()

        print("Received Data:", data)
        name = data.get("name")
        nickname = data.get("nickname")
        country_id = data.get("country_id")

        if name is None or nickname is None or country_id is None:
            print ("Girl no fields filled here!")
            return {"error":"Missing required fields. Either name, nickname or country id."},404
        
        else:
            new_learner = Learner(
                name = name,
                nickname = nickname,
                country_id = country_id
            )
            db.session.add(new_learner)
            db.session.commit()

            response_body = {
                "id" : new_learner.id,
                "name" : new_learner.name,
                "nickname" : new_learner.nickname,
                "country_id" : new_learner.country_id
            }
            print("Yay new learner created")
            response_status = 201
            response = make_response(jsonify(response_body),response_status)

            return response
   
api.add_resource(LearnerList, '/learners')    

class LearnerByID(Resource):
    def get(self, id):
        learner = Learner.query.get(id)

        if learner:
            response_body = {
                "id": learner.id,
                "name":learner.name,
                "nickname":learner.nickname,
                "country_id":learner.country_id
            }
            response_status = 200

        else:
            response_body = {"error" : f"Learner with ID {id} not found."}
            response_status = 404

        return make_response(jsonify(response_body), response_status)    

api.add_resource(LearnerByID, '/learner/<int:id>')


class CategoryList(Resource):
    def get(self):
        categories = Category.query.all()
        category_list = [
            {"id":category.id,
            "name":category.name,
            } for category in categories
        ]
        if categories:
            response_body = category_list
            response_status = 200
        else:
            response_body = {"error":"Categories not found"}
            response_status = 404
        response = make_response(jsonify(response_body),response_status)
        return response        
        
    def post(self):
        data = request.get_json()
        name = data.get("name")

        if name is None:
            return {"error":"Missing name which is a required fields."},404
        
        else:
            new_category = Category(
                name = name
            )
            db.session.add(new_category)
            db.session.commit()

            response_body = {
                "id" :new_category.id,
                "name":new_category.name
            }
            response_status = 201
            response = make_response(jsonify(response_body), response_status)
            return response

api.add_resource(CategoryList, '/categories')        


class CountryList(Resource):
    def get(self):
        countries = Country.query.all()
        country_list = [
            {"id":country.id,
            "name":country.name,
            } for country in countries
        ]
        if countries:
            response_body = country_list
            response_status = 200
        else:
            response_body = {"error":"Countries not found"}
            response_status = 404
        response = make_response(jsonify(response_body),response_status)
        return response        
        
    def post(self):
        data = request.get_json()
        name = data.get("name")

        if name is None:
            return {"error":"Missing name which is a required fields."},404
        
        else:
            new_country = Country(
                name = name
            )
            db.session.add(new_country)
            db.session.commit()

            response_body = {
                "id" :new_country.id,
                "name":new_country.name
            }
            response_status = 201
            response = make_response(jsonify(response_body), response_status)
            return response

api.add_resource(CountryList, '/countries')     

class ProficiencyLevelList(Resource):
    def get(self):
        proficiency_levels = ProficiencyLevel.query.all()
        return [level.to_dict() for level in proficiency_levels], 200

    def post (self):
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        learner_id = data.get("learner_id")
        card_id = data.get("card_id")

        learner = Learner.query.get(learner_id)
        card = Card.query.get(card_id)

        if not learner or not card:
            return{"error":"Learne or Card not found"}, 404
        
        new_level = ProficiencyLevel(
            name=name,
            description=description,
            learner_id=learner_id,
            card_id=card_id,
        )

        db.session.add(new_level)
        db.session.commit()

        return new_level.to_dict(),201

api.add_resource(ProficiencyLevelList, '/proficiencylevels')   

class ProficiencyLevelById(Resource):
    def get(self, id):
        proficiency_level = ProficiencyLevel.query.get(id)
        if not proficiency_level:
            return {'error':'Proficiency level not found'},404
        return proficiency_level.to_dict(), 200
    
    def patch (self, id):
        proficiency_level = ProficiencyLevel.query.get(id)
        if not proficiency_level:
            return{'error':'Proficiency level not found'}, 404

        data = request.get_json()
        if "name" in data:
            proficiency_level.name = data['name']   

        if "description" in data:
            proficiency_level.description= data["description"]

        if "learner_id" in data:
            learner = Learner.query.get(data['learner_id']) 
            if not learner:
                return{"error":"Learner not found"}, 404
            proficiency_level.learner_id = data["learner_id"]

        if "card_id" in data:
            card = Card.query.get(data["card_id"])
            if not card:
                return{"error":"Card not found"}, 404
            proficiency_level.card_id = data["card_id"] 

        db.session.commit()
        return proficiency_level.to_dict(), 200   

    def delete(self, id):
        proficiency_level = ProficiencyLevel.query.get(id)
        if not proficiency_level:
            return {"error":"Proficiency level not found"}, 404

        db.session.delete(proficiency_level)
        db.session.commit()          
        return{"message":"Proficiency level has been deleted successfully"}, 200
    
api.add_resource(ProficiencyLevelById, '/proficiencylevel/<int:id>')  

class CountryLearners(Resource):
    def get(self, country_id):
        # country = Country.query.get(country_id)
        country = Country.query.get(country_id)
        if not country:
            return {"error":"Country not found"}, 404
        
        learners = [learner.to_dict() for learner in country.learners]

        return {"country_id" : country.id, "country_name" : country.name, "learners": learners}, 200
    
api.add_resource(CountryLearners, '/country/<int:country_id>/learners') 
         

class LearnerCards(Resource):
    def get(self, learner_id):
        learner = Learner.query.get(learner_id)
        if not learner:
            return{"error":"Learner not found"}, 404
        
        cards = [card.to_dict() for card in learner.cards]

        return {"learner_id":learner.id, "name":learner.name, "cards":cards}, 200
    
api.add_resource(LearnerCards, '/learners/<int:learner_id>/cards')    
    
class CardLearners(Resource):
    def get(self, card_id):
        card = Card.query.get(card_id)
        if not card:
            return {"error":"Card not found"}, 404

        learners = [learner.to_dict() for learner in card.proficiencylevels]

        return {"card_id":card.id, "hanzi":card.hanzi, "learners":learners}, 200
       
api.add_resource(CardLearners, '/cards/<int:card_id>/learners')

class CategoryCards(Resource):
    def get(self, category_id):
        category=Category.query.get(category_id)
        if not category:
            return {"error":"Category not found"}, 404
        
        cards = [card.to_dict() for card in category.cards]

        return {"category_id":category.id, "cards":cards}, 200
    
api.add_resource(CategoryCards, "/category/<int:category_id>/cards")    

class CountryLearnersCards(Resource):
    def get(self, country_id):
        country = Country.query.get(country_id)
        if not country:
            return{"error":"Country not found"}, 404
        
        learners = Learner.query.filter_by(country_id=country_id).all()

        all_cards = []
        for learner in learners:
            for proficiency_level in learner.proficiencylevels:
                all_cards.append(proficiency_level.card.to_dict())

        return {"country_id":country.id, "country_name": country.name, "cards":all_cards}, 200
            
api.add_resource(CountryLearnersCards, '/country/<int:country_id>/cards')            

class CardsByCategory(Resource):
    def get(self, category_id):
        cards = Card.query.filter_by(category_id=category_id).all()
        if not cards:
            return{"message":"No cards found for this category"}, 404
        return jsonify([card.to_dict()for card in cards])
    
api.add_resource(CardsByCategory, '/category/<int:category_id>/cards')    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# GET ALL Cards /cards DONE
# POST Card /cards DONE
# GET Card by id /card/id DONE
# PATCH Card card/id DONE
# DELETE Card card/id DONE

# GET all Learners /users DONE
# POST Learner /learners DONE
# GET Learner by id /learner/id DONE

# GET all Categories /categories DONE
# POST Category /categories DONE
# # GET Category by id /level/id

# GET all Countries /countries
# # POST Country /countries
# # GET Country by id /countries/id

# GET all ProficiencyLevels /proficiencylevels DONE
# POST ProficiencyLevel /proficiencyLevels DONE
# GET ProficiencyLevel by id /proficiencylevel/id DONE
# PATCH ProficiencyLevel by id /proficiencylevel/id DONE
# DELETE ProficiencyLevel by id /proficiencylevel/id DONE
  