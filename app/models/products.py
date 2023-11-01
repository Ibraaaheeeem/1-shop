from app import db
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(124), nullable=False)
    skuList = db.Column(db.String(102400), nullable=False)
    defaultSku = db.Column(db.String(1024), nullable=False)
    defaultImageUrl = db.Column(db.String(1024), nullable=False)
    otherImagesUrl = db.Column(db.String(1024), nullable=False)
    productDescriptionUrl = db.Column(db.String, nullable=False)
    appliedProperties = db.Column(db.String)
    
    # Foreign keys to link to each of the five levels
    level1_id = db.Column(db.Integer, db.ForeignKey('level1.id'))
    level2_id = db.Column(db.Integer, db.ForeignKey('level2.id'))
    level3_id = db.Column(db.Integer, db.ForeignKey('level3.id'))
    level4_id = db.Column(db.Integer, db.ForeignKey('level4.id'))
    level5_id = db.Column(db.Integer, db.ForeignKey('level5.id'))

    # Define relationships to access each level
    level1 = db.relationship('Level1', backref='products_level1', foreign_keys=[level1_id])
    level2 = db.relationship('Level2', backref='products_level2', foreign_keys=[level2_id])
    level3 = db.relationship('Level3', backref='products_level3', foreign_keys=[level3_id])
    level4 = db.relationship('Level4', backref='products_level4', foreign_keys=[level4_id])
    level5 = db.relationship('Level5', backref='products_level5', foreign_keys=[level5_id])

    # def __init__(self, level1, level2, level3, level4, level5):
    #     self.level1 = level1
    #     self.level2 = level2
    #     self.level3 = level3
    #     self.level4 = level4
    #     self.level5 = level5