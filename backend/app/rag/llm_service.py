import ollama


class LLMService:
    def build_prompt(self, question: str, context: str) -> str:
        return f"""
        You are EduRAG, an AI assistant that answers questions about university documents.

        Use ONLY the information contained in the provided context.

        Instructions:
        - Carefully read all context before answering.
        - Answer the question using relevant information from the context.
        - The wording of the question does not need to exactly match the wording in the context.
        - You may summarize or explain information found in the context.
        - Do not use outside knowledge.
        - Do not invent information.
        - Keep the answer clear and concise.
        - If the context does not contain enough information to answer the question, respond exactly:
        "I couldn't find that information in the uploaded document."

        Context:
        ----------------
        {context}
        ----------------

        Question:
        {question}

        Answer:
        """

    def generate(self, prompt: str) -> str:
            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
    
            return response["message"]["content"]
    
llm_service = LLMService()