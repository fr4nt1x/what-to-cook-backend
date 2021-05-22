from tinydb import TinyDB
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage

from schemas.meal import Meal


class DB(object):
    MEAL_TABLE_NAME = "meals"
    CALENDAR_TABLE_NAME = "calendar"

    def __init__(self, path):
        TinyDB.default_table_name = self.MEAL_TABLE_NAME
        self.db = TinyDB(path, storage=CachingMiddleware(JSONStorage))

    def add_meal(self, meal: Meal):
        self.db.insert(meal.as_dict())

    def get_all_meals(self):
        return self.db.all()
