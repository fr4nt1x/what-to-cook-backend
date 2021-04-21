from database.db import DB
import os
import datetime


class TestDB:
    data_base_path = ()

    def test_add_meal(self, tmpdir):
        path = os.path.join(tmpdir, "db.json")
        db = DB(path)
        last_meal_date = datetime.date.today().isoformat()
        meal1 = {"name": "meal1 bla bla", "difficulty": 3, "count": 20, "last_date": last_meal_date}
        db.add_meal(meal1)
        last_meal_date = datetime.date(2021, 10, 12).isoformat()
        meal2 = {"name": "meal2-blü_blÖ", "difficulty": 2, "count": 1, "last_date": last_meal_date}
        db.add_meal(meal2)
        allMeals = db.get_all_meals()
        assert [meal1, meal2] == allMeals
