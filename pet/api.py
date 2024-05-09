
from flask.views import MethodView
from flask import jsonify, request, abort
from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match
#from app.decorators import app_required When adding security

import datetime
import uuid

from pet.models import Pet
from pet.templates import pet_obj, pets_obj
from pet.schema import schema

class PetAPI(MethodView):
    # decorators = [app_required] When adding security

    def __init__(self):
        self.PETS_PER_PAGE = 9999
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
            #pets = Pet.objects.filter(live=True) when we have implemented live flag
            pets = Pet.objects  # get all here

            #for x in pets:
                #print(x)

            page = 1
            pets = pets.paginate(page=page, per_page=self.PETS_PER_PAGE)

            response = {
                "result": "ok",
                "pets": pets_obj(pets)
                }
            return jsonify(response), 200
        
    def post(self):
        pet_json = request.json
        error = best_match(Draft4Validator(schema).iter_errors(pet_json))
        if (error):
            return jsonify({"error:": error.message}), 400
        '''
        store = Store.objects.filter(external_id=pet_json.get('store')).first()
        if not store:
            error = {
                "code": "Store not found"
            }
            return jsonify({'error': error}), 400
        '''

        try:
            received_date = datetime.datetime.strptime(
                pet_json.get('received_date'), "%Y-%m-%dT%H:%M:%SZ")
        except:
            return jsonify({"error": "INVALID_DATE"}), 400
        
        pet = Pet(
            external_id=str(uuid.uuid4()),
            name=pet_json.get('name'),
            received_date=received_date
        ).save()
        response={
            "result": "ok",
            "pet": pet_obj(pet)
        }
        return jsonify(response), 201
