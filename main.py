from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

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
    if format == "json":
        return {"initial_date": initial_date, "final_date": final_date}
    elif format == "text":
        return f"Inicial: {initial_date}, Final: {final_date}"
    else:
        return {"error": "Formato inválido, use 'json' ou 'text'"}