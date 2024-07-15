from peewee import *

database = SqliteDatabase('database.db')

class Outlet(Model):
    name = CharField()
    address = CharField()
    waze_link = CharField()
    operating_hours = CharField()
    latitude = DecimalField(null=True)
    longitude = DecimalField(null=True)

    class Meta:
        database = database