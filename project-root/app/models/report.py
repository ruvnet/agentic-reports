from pydantic import BaseModel

class Report(BaseModel):
    topic: str
    content: str
