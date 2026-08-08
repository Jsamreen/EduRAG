from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    page: int
    score: float
    text: str