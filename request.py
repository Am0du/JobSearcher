from pydantic import BaseModel


class Item(BaseModel):
    job_title: str
    location: str


class Mail(BaseModel):
    search_result: list
    email_address: str
    search_title: str


class Status(BaseModel):
    id: str
