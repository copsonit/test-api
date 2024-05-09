def pet_obj(pet, nostore=True):
    pet_obj = {
        "id": pet.external_id,
        "name": pet.name
    }

def pets_obj(pets, nostore=True):
    pets_obj = []
    for pet in pets.items:
            pets_obj.append(pet_obj(pet, nostore))
    return pets_obj