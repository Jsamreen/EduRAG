from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str

class Source(BaseModel):
    document: str
    page: int


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
