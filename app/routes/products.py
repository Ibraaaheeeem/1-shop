import app
from app import db
from ..models.property import Property
from ..models.products import Product
from ..models.levels import Level1, Level2, Level3, Level4, Level5
from flask import Blueprint, request, jsonify

products_bp = Blueprint('products', __name__)

@products_bp.route('', methods=['POST'])
def save_product():
    data = request.get_json()
    product = Product.query.filter_by(name=data["name"]).first()
    if product:
        return jsonify({'message':'Product name exists already', 'error': 'True', 'extras': {'product_id': product.id}}), 201
    else:
        product = Product(
        name = data["name"],
        level1_id = data["level_ids"][0],
        level2_id = data["level_ids"][1],
        level3_id = data["level_ids"][2],
        level4_id = data["level_ids"][3],
        level5_id = data["level_ids"][4],
        skuList = data["sku_list"],
        defaultSku = data["default_sku"],
        defaultImageUrl = data["default_image_url"],
        otherImagesUrl = data["other_images_url"],
        productDescriptionUrl = data["product_description_url"],
        appliedProperties = data["applied_properties"]
        )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message':'Product saved', 'error': 'False', 'extras': {'product_id': product.id}}), 201

@products_bp.route('/<int:product_id>', methods=['PATCH'])
def edit_product(product_id):
    data = request.get_json()
    existing = Product.query.get(product_id)

    if existing is None:
        return jsonify({'message':'Product not found', 'error': 'True'}), 404

    try:
        # Update the product attributes with data from the JSON request
        existing.name = data.get("name", existing.name)
        existing.level1_id = data.get("level_ids")[0] if "level_ids" in data else existing.level1_id
        existing.level2_id = data.get("level_ids")[1] if "level_ids" in data else existing.level2_id
        existing.level3_id = data.get("level_ids")[2] if "level_ids" in data else existing.level3_id
        existing.level4_id = data.get("level_ids")[3] if "level_ids" in data else existing.level4_id
        existing.level5_id = data.get("level_ids")[4] if "level_ids" in data else existing.level5_id
        existing.skuList = data.get("sku_list", existing.skuList)
        existing.defaultSku = data.get("default_sku", existing.defaultSku)
        existing.defaultImageUrl = data.get("default_image_url", existing.defaultImageUrl)
        existing.otherImagesUrl = data.get("other_images_url", existing.otherImagesUrl)
        existing.productDescriptionUrl = data.get("product_description_url", existing.productDescriptionUrl)
        existing.appliedProperties = data.get("applied_properties", existing.appliedProperties)

        db.session.commit()
        return jsonify({'message':'Product edited', 'error': 'False', 'extras': {'product_id': product_id}}), 200
    except Exception as e:
        db.session.rollback()  # Roll back changes in case of an error
        return jsonify({'message': 'Error editing product', 'error': 'True', 'extras': {'error_message': str(e)}}), 500

@products_bp.route('/level/<int:level_number>/id/<int:level_id>', methods=['GET'])
def get_similar_products(level_number, level_id):
    
    products = None
    if level_number == 1:
        products = Product.query.filter_by(level1_id=level_id).all()
    elif level_number == 2:
        products = Product.query.filter_by(level2_id=level_id).all()
    elif level_number == 3:
        products = Product.query.filter_by(level3_id=level_id).all()
    elif level_number == 4:
        products = Product.query.filter_by(level4_id=level_id).all()
    elif level_number == 5:
        products = Product.query.filter_by(level5_id=level_id).all()
    
    products_length = products
    return jsonify([{'id': product.id, 'name': product.name} for product in products]), 200

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    
    product = Product.query.get(product_id)
    # if level_number == 1:
    #     products = Product.query.filter_by(level1_id=level_id).all()
    # elif level_number == 2:
    #     products = Product.query.filter_by(level2_id=level_id).all()
    # elif level_number == 3:
    #     products = Product.query.filter_by(level3_id=level_id).all()
    # elif level_number == 4:
    #     products = Product.query.filter_by(level4_id=level_id).all()
    # elif level_number == 5:
    #     products = Product.query.filter_by(level5_id=level_id).all()
    product = {
        'name': product.name,
        'sku_list': product.skuList,
        'default_sku': product.defaultSku,
        'default_image_url': product.defaultImageUrl,
        'other_images_url': product.otherImagesUrl,
        'product_description_url': product.productDescriptionUrl,
        'level_ids':[product.level1_id, product.level2_id, product.level3_id, product.level4_id, product.level5_id],
        'applied_properties': product.appliedProperties
        }
    level1_name = Level1.query.get(product['level_ids'][0]).name
    level2_name = Level2.query.get(product['level_ids'][1]).name
    level3_name = Level3.query.get(product['level_ids'][2]).name
    level4_name = Level4.query.get(product['level_ids'][3]).name
    level5_name = Level5.query.get(product['level_ids'][4]).name
    #level1_name = Level1.query.filter_by(level1_id=product.level1_id).first().name
    # level2_name = Level2.query.get(product.level2_id)["name"]
    # level3_name = Level3.query.get(product.level3_id)["name"]
    # level4_name = Level4.query.get(product.level4_id)["name"]
    # level5_name = Level5.query.get(product.level5_id)["name"]
    level_list = [level1_name, level2_name, level3_name, level4_name, level5_name]
    return jsonify({'message':'Success', 'error': 'False', 'extras': {'product': product, 'product_id': product_id, 'level_list': level_list}}), 200