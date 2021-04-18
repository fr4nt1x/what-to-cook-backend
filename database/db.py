from tinydb import TinyDB


class DB(object):
    MEAL_TABLE_NAME = "meals"
    CALENDAR_TABLE_NAME = "calendar"

    def __init__(self, path):
        TinyDB.default_table_name = self.MEAL_TABLE_NAME
        self.db = TinyDB(path)

    def add_meal(self, meal):
        self.db.insert(meal)

    def get_all_meals(self):
        return self.db.all()
