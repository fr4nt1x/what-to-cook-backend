from tinydb import TinyDB, Query
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage

from schemas.meal import Meal


class DB(object):
    MEAL_TABLE_NAME = "meals"
    CALENDAR_TABLE_NAME = "calendar"

    def __init__(self, path):
        TinyDB.default_table_name = self.MEAL_TABLE_NAME
        self.db = TinyDB(path, storage=CachingMiddleware(JSONStorage), indent=4)

    def add_meal(self, meal: Meal):
        self.db.insert(meal.as_dict())

    def get_all_meals(self):
        return self.db.all()

    def change_tags_for_meal(self, meal: Meal):
        meal_query = Query()
        self.db.update({"tags": meal.tags}, meal_query.name == meal.name)

    def close(self):
        self.db.close()
