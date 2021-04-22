from pydantic import BaseModel
import datetime


class Meal(BaseModel):
    name: str
    difficulty: int
    count: int
    last_date: datetime.date

    @staticmethod
    def from_dict(input_dict):
        return Meal(name=input_dict["name"], difficulty=input_dict["difficulty"], count=input_dict["count"],
                    last_date=input_dict["last_date"])

    def as_dict(self):
        return {'name': self.name, 'difficulty': self.difficulty, 'count': self.count,
                'last_date': self.last_date.isoformat()}
