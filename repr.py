from sqlmodel import SQLModel, Field
from uuid import uuid4

def gen_id() -> str:
    return str(uuid4())

class MonologicalData(SQLModel, table=True):
    prompt: str = Field(primary_key=True)
    response: str = Field()