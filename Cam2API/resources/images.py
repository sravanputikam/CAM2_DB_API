from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.image import ImageModel
from modules.camera import CameraModel


class CameraList(Resource):

    @jwt_required()
    def get(self):

        cameras = CameraModel.camera_list()
        if cameras:
            camera = {
                "message": "Successful Request",
                "camera_list": []
            }

            for row in cameras:
                camera["camera_list"].append(row.json())

            return camera, 200
        else:
            return {'message': 'cameras not found'}, 404


class ImageList(Resource):

    @jwt_required()
    def get(self, camera_id):

        check_id = CameraModel.check_camera(camera_id)
        if check_id is None:
            return {'message': 'Camera Id is Invalid/Not Found'}, 400
        images = ImageModel.find_by_camera_id(camera_id)
        if images:
            image_list = list()
            for image_row in images:
                image_list.append(image_row.json)
                return {
                    "message": "Successful Request",
                    "camera_id": camera_id,
                    "image_list": image_list
                }, 200
        else:
            return {'message': 'Images not found'}, 404


class Dataset(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("dataset",
                        type=str,
                        reqruied=False,
                        )

    @jwt_required()
    def get(self,dataset):
        if dataset is None:
            list = ImageModel.get_dataset_list()




