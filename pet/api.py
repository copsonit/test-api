
from flask.views import MethodView
from flask import jsonify, request, abort
#from app.decorators import app_required When adding security

from pet.models import Pet
from pet.templates import pet_obj

class PetAPI(MethodView):
    # decorators = [app_required] When adding security

    def __init__(self):
        self.PETS_PER_PAGE = 10
        if (request.method != 'GET' and request.method != 'POST') and not request.json:
            abort(400)

    def get(self, pet_id):
        if (pet_id):
            pet = Pet.objects.filter(external_id=pet_id).first()
            if pet:
                response = {
                    "result": "ok",
                    "pet": pet_obj(pet)
                }
                return jsonify(response), 200
            else:
                return jsonify({}), 404
        else:
            return jsonify({}), 200
        