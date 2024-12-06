from sqlalchemy import create_engine, insert, select
from sqlalchemy.orm import Session

from models import Base, Template

import json


engine = create_engine("sqlite:///test.db")

Base.metadata.create_all(engine)
session = Session(engine)


def check_db() -> None:
    "Проверка бд на наличие шаблонов"
    
    stmt = select(Template)
    if not session.scalar(stmt):
        insert_templates_db()
        
def insert_templates_db() -> None:
    "Вставка шаблонов в БД"
    
    data = {
        "User":{
            "name": "str",
            "phone": "phone",
            "date": "date",
            "email": "email"
        },
        "Email": {
            "name": "str",
            "email": "email"
        },
        "Phone": {
            "name": "str",
            "phone": "phone"
        },
        "Birthday": {
            "name": "str",
            "date": "date"
        }
    }
    session.execute(
        insert(Template),
        [
            {"name": "User", "template": json.dumps(data["User"])},
            {"name": "Email", "template": json.dumps(data["Email"])},
            {"name": "Phone", "template": json.dumps(data["Phone"])},
            {"name": "Birthday", "template": json.dumps(data["Birthday"])},
        ]
    )
    session.commit()
