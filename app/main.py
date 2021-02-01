from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class LogEntry(BaseModel):
    reporting_item: str
    log: Optional[str] = None


app = FastAPI()


@app.post("/loginput/")
async def log_entry(item: LogEntry):
    return log_entry
