from app import db

class BaseLevel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(1024), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    item_count = db.Column(db.Integer)
    image_url = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'item_count': self.item_count,
            'image_url': self.image_url
        }
        
class Level5(BaseLevel):
    __tablename__ = 'level5'
    parent_id = db.Column(db.Integer, db.ForeignKey('level4.id'))
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'item_count': self.item_count,
            'image_url': self.image_url,
            'parent_id': self.parent_id
        }

class Level4(BaseLevel):
    __tablename__ = 'level4'
    parent_id = db.Column(db.Integer, db.ForeignKey('level3.id'))
    children = db.relationship('Level5', backref='parent', lazy=True, cascade='all, delete-orphan')
    def get_children(self):

        return self.children
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'item_count': self.item_count,
            'image_url': self.image_url,
            'parent_id': self.parent_id
        }


class Level3(BaseLevel):
    __tablename__ = 'level3'
    parent_id = db.Column(db.Integer, db.ForeignKey('level2.id'))
    children = db.relationship('Level4', backref='parent', lazy=True, cascade='all, delete-orphan')
    def get_children(self):

        return self.children
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'item_count': self.item_count,
            'image_url': self.image_url,
            'parent_id': self.parent_id
        }


class Level2(BaseLevel):
    __tablename__ = 'level2'
    parent_id = db.Column(db.Integer, db.ForeignKey('level1.id'))
    children = db.relationship('Level3', backref='parent', lazy=True, cascade='all, delete-orphan')
    def get_children(self):
        return self.children
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'item_count': self.item_count,
            'image_url': self.image_url,
            'parent_id': self.parent_id
        }


class Level1(BaseLevel):
    __tablename__ = 'level1'
    children = db.relationship('Level2', backref='parent', lazy=True, cascade='all, delete-orphan')
    
    def get_children(self):
        return self.children
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'item_count': self.item_count,
            'image_url': self.image_url
        }