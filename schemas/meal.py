import datetime
from typing import List

from pydantic import BaseModel


class Meal(BaseModel):
    name: str
    tags: List[str]
    count: int
    last_dates: List[datetime.date]

    @staticmethod
    def from_dict(input_dict):
        return Meal(name=input_dict["name"], tags=input_dict["tags"], count=input_dict["count"],
                    last_dates=input_dict["last_dates"])

    def as_dict(self):
        return {'name': self.name, 'tags': self.tags, 'count': self.count,
                'last_dates': [d.isoformat() for d in sorted(self.last_dates)]}
