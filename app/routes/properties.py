import app
from ..models.property import Property
from flask import Blueprint

properties_bp = Blueprint('properties', __name__)

@properties_bp.route('', methods=['GET'])
def get_all_properties():
    properties = Property.query.all()
    properties_list = [property.serialize() for property in properties]
    print(properties_list)
    return properties_list
