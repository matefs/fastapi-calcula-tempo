from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from Utils.Utils import validate_JSON_format

app = FastAPI()
# Todo: Never return as a datetime object, always return as numbers | days: 1 | hours: 2 | minutes: 3 | seconds: 4

@app.get("/datetime/difference")
async def return_date_time_difference(
        initial_date: datetime,
        final_date: datetime,
        format: Optional[str] = "json"  # Adicionando um parâmetro opcional para especificar o formato
):
    date_time_difference:datetime = None 

    if initial_date > final_date: return {"error": "Data inicial não pode ser maior do que data final"}

    if (validate_JSON_format(format)):
        datetime_difference = final_date - initial_date
        # time_difference_in_days = datetime_difference.days
        # time_difference_in_hours = datetime_difference.hours
        # time_difference_in_months = datetime_difference.months
        time_difference_in_seconds: float = date_time_difference.total_seconds()
        return {"initial_date": initial_date, "final_date": final_date, "date_time_difference": str(date_time_difference), "seconds": time_difference_in_seconds}
    
    return {"error": "Formato inválido, use 'json' ou 'text'"}


@app.get('/', include_in_schema=False)
async def main():
    return RedirectResponse(url="/docs")

