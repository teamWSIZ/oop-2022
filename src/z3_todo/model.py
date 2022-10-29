from dataclasses import dataclass
from datetime import datetime, timedelta, date
from uuid import UUID, uuid4

# dataclasses


@dataclass
class Todo:
    message: str
    created: datetime = datetime.now()
    due_date: datetime = (datetime.now() + timedelta(days=7))
    owner_id: int = 0
    todo_id: UUID = uuid4()
    is_done = False


def date_from_day(the_date: date):
    return datetime(year=the_date.year, month=the_date.month, day=the_date.day)


if __name__ == '__main__':
    # t = Todo('Lorem ipsum', datetime())
    # s = 'abcd'
    # dt = datetime.now()
    # print(dt)
    # dt += timedelta(days=1)
    # print(dt)
    # print(s[2])
    # d_ = date(2022, 10, 29)
    # dd = date_from_day(d_)
    # print(dd)
    # print(isinstance(dd, datetime)) # sprawdza czy dany obiekt(referencja) jest wybranego typu

    td = Todo('Lorem ipsum')
    print(td)



