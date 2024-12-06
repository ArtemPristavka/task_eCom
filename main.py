from fastapi import FastAPI, Body
from typing import Dict
from manager import Manager
from engine_db import check_db
import uvicorn


app = FastAPI()


@app.post("/get_form")
async def get_form(data=Body()) -> Dict[str, str]: # type: ignore
    "Для проверки формы"
    
    manager = Manager(input_data=data)
    response = manager.search_template()
    
    if response is None:
        return {"Error": "The template was not found"}
    
    return {"Template": response}


if __name__ == "__main__":
    check_db()
    uvicorn.run(app)