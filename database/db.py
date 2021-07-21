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
        return True

    def remove_date_from_meal(self, meal: Meal, date: str):
        meal_query = Query()
        found_meal = self.db.search(meal_query.name == meal.name)
        if len(found_meal) == 1:
            found_meal = found_meal[0]
            if date in found_meal['last_dates']:
                found_meal['last_dates'].remove(date)
                self.db.update(
                    {"last_dates": sorted(found_meal['last_dates'])},
                    meal_query.name == meal.name)
                return True
        return False

    def update_dates_for_meal(self, meal: Meal):
        meal_query = Query()
        self.db.update({"last_dates": list(set([d.isoformat() for d in sorted(meal.last_dates)]))},
                       meal_query.name == meal.name)
        return True

    def get_all_meals(self):
        return self.db.all()

    def change_tags_for_meal(self, meal: Meal):
        meal_query = Query()
        self.db.update({"tags": meal.tags}, meal_query.name == meal.name)
        return True

    def close(self):
        print("close")
        self.db.close()
