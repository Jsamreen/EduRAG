from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    limit: int = Field(default=4, ge=1, le=10)


class SearchResult(BaseModel):
    page: int
    score: float
    text: str
    document_id: str
    document_name: str


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str