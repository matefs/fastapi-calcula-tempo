from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from Utils.Utils import validate_JSON_format

app = FastAPI()

class DateParams(BaseModel):
    initial_date: datetime
    final_date: datetime

#Todo: calculate the difference between the two dates

@app.get("/datetime/difference")
async def return_date_difference(
    initial_date: datetime,
    final_date: datetime,
    format: Optional[str] = "json"  # Adicionando um parâmetro opcional para especificar o formato
):
    if(validate_JSON_format(format)):
        date_difference : datetime = final_date - initial_date
        return { "initial_date": initial_date, "final_date": final_date, "date_difference": str(date_difference) }

    return {"error": "Formato inválido, use 'json' ou 'text'"}
