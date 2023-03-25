from pydantic import BaseModel


class Site(BaseModel):
    host_name: str
    source_code: bytes
