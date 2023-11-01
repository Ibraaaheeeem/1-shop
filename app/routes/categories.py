import app
from app import db
from ..models.levels import *
from flask import Blueprint, jsonify, request

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/levels/<int:level_number>', methods=['GET'])
def get_categories(level_number):
    parent_id = request.args["parent_id"]
    print(parent_id)
    print(level_number)
    categories = None
    categories_list = []
    if level_number == 1:
        categories = Level1.query.all()
        
    elif level_number == 2:
        categories = Level2.query.filter_by(parent_id=parent_id).all()
        
    elif level_number == 3:
        categories = Level3.query.filter_by(parent_id=parent_id).all()
        
    elif level_number == 4:
        categories = Level4.query.filter_by(parent_id=parent_id).all()
        
    elif level_number == 5:
        categories = Level5.query.filter_by(parent_id=parent_id).all()
        
    if categories:
        categories_list = [category.serialize() for category in categories]
    else:
        categories_list = []
    print(f'list{level_number}')
    print(categories_list)
    return categories_list, 200


@categories_bp.route('/levels/<int:level_number>', methods=['POST'])
def new_category(level_number):
    
    level_data = request.get_json()
    
    print(level_data)
    level = None
    categories = None

    if level_number == 1:
        level_exists = Level1.query.filter_by(name=level_data["name"]).first()
        
        if level_exists:
            return jsonify({'message':'Level already exist', 'error': 'True', 'extras': {'level_id': level_exists.id}}), 409
        
        level = Level1(
            name = level_data["name"],
            description = level_data["description"],
            image_url = level_data["image_url"]
            )
        db.session.add(level)
        db.session.commit()
        categories = Level1.query.all()
    elif level_number == 2:
        level_exists = Level2.query.filter_by(name=level_data["name"]).first()
        if level_exists:
            return jsonify({'message':'Level already exist', 'error': 'True', 'extras': {'level_id': level_exists.id}}), 409
        
        parent_level_exists = Level1.query.get(level_data["parent_id"])
        if parent_level_exists == None:
            return jsonify({'message':'Invalid Parent level', 'error': 'True', 'extras': {'level_id': level_data["parent_id"]}}), 400

        level = Level2(
            name = level_data["name"],
            description = level_data["description"],
            image_url = level_data["image_url"],
            parent_id = level_data["parent_id"]
            )
        db.session.add(level)
        db.session.commit()
        categories = Level2.query.filter_by(parent_id=level_data["parent_id"]).all()
    elif level_number == 3:
        level_exists = Level3.query.filter_by(name=level_data["name"]).first()
        
        if level_exists:
            return jsonify({'message':'Level already exist', 'error': 'True', 'extras': {'level_id': level_exists.id}}), 409
        level = Level3(
            name = level_data["name"],
            description = level_data["description"],
            image_url = level_data["image_url"],
            parent_id = level_data["parent_id"]
            )
        db.session.add(level)
        db.session.commit()
        categories = Level3.query.filter_by(parent_id=level_data["parent_id"]).all()
    elif level_number == 4:
        level_exists = Level4.query.filter_by(name=level_data["name"]).first()
        if level_exists:
            return jsonify({'message':'Level already exist', 'error': 'True', 'extras': {'level_id': level_exists.id}}), 409
        level = Level4(
            name = level_data["name"],
            description = level_data["description"],
            image_url = level_data["image_url"],
            parent_id = level_data["parent_id"]
            )
        db.session.add(level)
        db.session.commit()
        categories = Level4.query.filter_by(parent_id=level_data["parent_id"]).all()
    elif level_number == 5:
        level_exists = Level5.query.filter_by(name=level_data["name"]).first()
        if level_exists:
            return jsonify({'message':'Level already exist', 'error': 'True', 'extras': {'level_id': level_exists.id}}), 409
        
        level = Level5(
            name = level_data["name"],
            description = level_data["description"],
            image_url = level_data["image_url"],
            parent_id = level_data["parent_id"]
            )
        db.session.add(level)
        db.session.commit()
        categories = Level5.query.filter_by(parent_id=level_data["parent_id"]).all()
    print((categories))
    return jsonify({'message':'successful', 'error': 'False', 'extras': {'level_id': level.parent_id, 'categories': [category.serialize() for category in categories]}}), 201