from db import db


class ImageModel(db.Model):

    __tablename__ = "Image"

    image_id = db.Column(db.String(50))
    time_stamp = db.Column(db.Time)
    date = db.Column(db.Interval)
    file_path = db.Column(db.String(100))
    file_type = db.Column(db.String(10))
    file_size = db.Column(db.String(10))
    date_modified = db.Column(db.Interval)
    data_set = db.Column(db.String(50))
    is_labeled = db.Column(db.Boolean)

    camera_id = db.Column(db.String(50),db.ForeignKey('camera.id'))
    camera = db.relationship("CameraModel")

    @classmethod
    def find_by_camera_id(cls, camera_id):
        return cls.query.filter_by(camera_id=camera_id).all

    @classmethod
    def find_by_dataset(cls, dataset):
        return cls.query.filter_by(data_set=dataset).all

    @classmethod
    def get_dataset_list(cls):
        return cls.query(cls.data_set).distinct()

    def __init__(self):
        pass

    def json(self):
        pass

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()