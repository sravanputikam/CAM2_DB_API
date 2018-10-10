from db import db


class CameraModel(db.Model):
    __tablename__ = "Camera"

    image_id = db.Column(db.String(50), primary_key=True)
    is_indoor = db.Column(db.Boolean)
    objects = db.Column(db.String)

    def __init__(self,image_id,is_indoor,objects):
        self.image_id = image_id
        self.is_indoor = is_indoor
        self.objects = objects

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()