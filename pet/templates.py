def pet_obj(pet, nostore=True):
    pet_obj = {
        "id": pet.external_id,
        "name": pet.name,
        "received_date":  str(pet.received_date.isoformat()[:19]) +"Z"
    }
    return pet_obj

def pets_obj(pets_paginated, nostore=True):
    pets_obj = []
    for pet in pets_paginated.items:  # items only exists when we have paginated the queryset
            pets_obj.append(pet_obj(pet, nostore))
    return pets_obj