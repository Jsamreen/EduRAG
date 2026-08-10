from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse, Source
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
        # 1. Retrieve relevant chunks
        results = retrieval_service.search(
            query=request.question,
            limit=4
        )

        # 2. Build context
        context = "\n\n".join(
            document.page_content
            for document, score in results
        )

        # 3. Build prompt
        prompt = llm_service.build_prompt(
            question=request.question,
            context=context
        )

        # 4. Generate answer
        answer = llm_service.generate(prompt)

        # 5. Collect unique sources
        sources = []

        seen_sources = set()

        for document, score in results:
            document_name = document.metadata.get(
                "document_name",
                "Unknown document"
            )

            page = document.metadata.get(
                "page",
                0
            )

            source_key = (
                document_name,
                page
            )

            if source_key not in seen_sources:
                seen_sources.add(source_key)

                sources.append(
                    Source(
                        document=document_name,
                        page=page
                    )
                )

        return ChatResponse(
            answer=answer,
            sources=sources
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to generate an answer."
        )