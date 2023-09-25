#!/usr/bin/env python3


from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from hero import Hero
from heroPower import HeroPower
from power import Power
from config import db
from routes import create_app


# #app initialization
app=create_app()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hero.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/heroes', methods=['GET'])
def heroes():
    heroes = []
    for hero in Hero.query.all():
         hero_dict = {
            "name": hero.name,
             "super_name": hero.super_name,
              
        }
         heroes.append(hero_dict)
    
    response = make_response(
        jsonify(heroes),
        200
    )        
    return response

@app.route('/powers', methods=['GET'])
def powers():
   pws=[]
   for power in Power.query.all():
       power_dict = {
           "name": power.name, "description": power.description

       }
       pws.append(power_dict)
   response = make_response(
        jsonify(pws),
        200
    )        
   return response   
    
    

@app.route('/add', methods = ['POST'])
def add_heropower() :
    data=request.get_json()
    #create new instance
    new_heropower = HeroPower (hero_id = data['hero_id'], power_id = data['power_id'], strength = data['strength'] )
    #save to database
    db.session.add(new_heropower)
    db.session.commit()
    return jsonify({"message":"HeroPower added"})

       

@app.route('/powers/<int:id>', methods = ['PATCH'])
def update_power(id) :
 power = Power.query.get(id)
 try:
  data = request.get_json() 
  power.description = data["description"]
  db.session.commit()
  return jsonify({"msg": "succesfull"})
 except Exception as e:
    db.session.rollback() 
    return jsonify({"errors": "validation errors"})




if __name__ == '__main__':
    app.run(port=5555)



# from flask import Flask, make_response
# from flask_migrate import Migrate
# from routes import create_app

# from models import db, Hero

# #app initialization
# app=create_app()

# #migrations

# app.config['SQLALCHEMY_DATABASE_URI ']= 'sqlite:///hero.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/')
# def home():
#     return ''


# if __name__ == '__main__':
#     app.run(debug=True,port=5555)
