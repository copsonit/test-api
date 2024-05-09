from application import db

class Pet(db.Document):
    external_id = db.StringField(db_field="ei")
    name = db.StringField(db_field="n")
    received_date = db.DateTimeField(db_field="rd")