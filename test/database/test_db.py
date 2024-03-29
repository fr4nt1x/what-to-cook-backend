import datetime
import os
from datetime import timedelta
from random import randrange, randint, sample

from database.db import DB
from schemas.meal import Meal


class TestDB:
    data_base_path = ()

    @staticmethod
    def get_random_date():
        start_date = datetime.date(2021, 1, 1)
        end_date = datetime.date(2021, 12, 31)
        delta = end_date - start_date
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)

        return start_date + timedelta(seconds=random_second)

    def test_add_meal(self, tmpdir):
        path = os.path.join(tmpdir, "db.json")
        db = DB(path)
        last_meal_date = datetime.date.today().isoformat()
        last_meal_date2 = datetime.date(2021, 10, 12).isoformat()
        meal1 = {"name": "meal1 bla bla", "tags": ["easy"], "count": 20, "last_dates": [last_meal_date]}
        db.add_meal(Meal.from_dict(meal1))
        meal2 = {"name": "meal2-blü_blÖ", "tags": ["easy", "medium"], "count": 1,
                 "last_dates": [last_meal_date, last_meal_date2]}
        db.add_meal(Meal.from_dict(meal2))
        all_meals = db.get_all_meals()
        assert [meal1, meal2] == all_meals

    def test_change_tags_for_meal(self, tmpdir):
        path = os.path.join(tmpdir, "db.json")
        db = DB(path)
        last_meal_date = datetime.date.today().isoformat()
        meal1 = {"name": "meal1 bla bla", "tags": ["easy"], "count": 20, "last_dates": [last_meal_date]}
        db.add_meal(Meal.from_dict(meal1))
        last_meal_date = datetime.date(2021, 10, 12).isoformat()
        meal2 = {"name": "meal2-blü_blÖ", "tags": ["easy", "medium"], "count": 1, "last_dates": [last_meal_date]}
        db.add_meal(Meal.from_dict(meal2))
        tags = ["new"]
        meal2['tags'] = tags
        db.change_tags_for_meal(Meal.from_dict(meal2))
        all_meals = db.get_all_meals()
        assert all_meals[1]["tags"] == tags

    def test_remove_date_from_meal(self, tmpdir):
        path = os.path.join(tmpdir, "db.json")
        db = DB(path)
        last_meal_date = datetime.date.today().isoformat()
        second_meal_date = last_meal_date
        meal1 = {"name": "meal1 bla bla", "tags": ["easy"], "count": 20, "last_dates": [last_meal_date]}
        db.add_meal(Meal.from_dict(meal1))
        last_meal_date = datetime.date(2021, 10, 12).isoformat()
        meal2 = {"name": "meal2-blü_blÖ", "tags": ["easy", "medium"], "count": 1,
                 "last_dates": [second_meal_date, last_meal_date]}
        db.add_meal(Meal.from_dict(meal2))
        db.remove_date_from_meal(Meal.from_dict(meal2), second_meal_date)
        all_meals = db.get_all_meals()
        assert all_meals[1]["last_dates"] == [last_meal_date]

    """Not a test. For database creation"""

    def many_meals(self, tmpdir):
        db = DB("db.json")
        possible_tags = ["Tag_{}".format(i) for i in range(1, 10)]

        for i in range(1, 500):
            possible_dates = [self.get_random_date() for i in range(1, 10)]
            j = randint(0, 4)
            number_of_dates = randint(0, 5)
            last_dates = sorted(list(set(sample(possible_dates, k=number_of_dates))))
            tags = sample(possible_tags, k=j)
            meal = {"name": "Meal{}".format(i), "tags": tags, "count": 0, "last_dates": last_dates}
            db.add_meal(Meal.from_dict(meal))
        db.close()
        print(db.get_all_meals())
