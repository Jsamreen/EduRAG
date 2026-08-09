from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.rag.retrieval_service import retrieval_service
from app.rag.llm_service import llm_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    try:

        # Step 1: Retrieve relevant chunks
        results = retrieval_service.search(
            query=request.question,
            limit=4
        )

        # Step 2: Combine chunks into context
        context = "\n\n".join(
            document.page_content
            for document, score in results
        )

        # Step 3: Build prompt
        prompt = llm_service.build_prompt(
            question=request.question,
            context=context
        )

        # Step 4: Generate answer
        answer = llm_service.generate(prompt)

        return ChatResponse(
            answer=answer
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )