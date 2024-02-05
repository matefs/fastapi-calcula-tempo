from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from Utils.Utils import validate_JSON_format

app = FastAPI()


class DateParams(BaseModel):
    initial_date: datetime
    final_date: datetime


# Todo: calculate the difference between the two dates

@app.get("/datetime/difference")
async def return_date_difference(
        initial_date: datetime,
        final_date: datetime,
        format: Optional[str] = "json"  # Adicionando um parâmetro opcional para especificar o formato
):
    if (validate_JSON_format(format)):
        date_difference: datetime = final_date - initial_date
        time_difference_in_seconds: float = date_difference.total_seconds()
        return {"initial_date": initial_date, "final_date": final_date, "date_difference": str(date_difference), "seconds": time_difference_in_seconds}

    return {"error": "Formato inválido, use 'json' ou 'text'"}

@app.get('/datetime/sum')
async def return_date_sum(initial_date: datetime, final_date: datetime, format: Optional[str] = "json"):
    if (validate_JSON_format(format)):
        date_sum: timedelta = final_date + initial_date
        return {"initial_date": initial_date, "final_date": final_date, "date_sum": str(date_sum) }
    return {"error": "Formato inválido, use 'json' ou 'text'"}

@app.get('/')
async def main():
    return RedirectResponse(url="/docs")