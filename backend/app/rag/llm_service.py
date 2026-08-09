import logging

import ollama

logger = logging.getLogger(__name__)


class LLMService:
    """Generate answers using Ollama."""

    def __init__(self):
        self.model = "llama3.2:3b"

    def generate_answer(
        self,
        question: str,
        context: str,
    ) -> str:
        prompt = f"""
You are EduRAG, an AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply:

"I couldn't find the answer in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        answer = response["message"]["content"]

        logger.info("Generated answer using Ollama.")

        return answer.strip()


llm_service = LLMService()