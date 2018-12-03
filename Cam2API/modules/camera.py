from db import db


class CameraModel(db.Model):
    __tablename__ = "Camera"

    camera_id = db.Column(db.String(50), primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def __init__(self):
        pass

    @classmethod
    def camera_list(cls):
        return cls.query.all

    @classmethod
    def check_camera(cls, camera_id):
        return cls.query.filter(camera_id=camera_id).first

    def json(self):
        return {
            "camera_id": self.camera_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city": self.city,
            "country": self.country
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

