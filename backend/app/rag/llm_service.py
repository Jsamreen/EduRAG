import ollama


class LLMService:
    def build_prompt(self, question: str, context: str) -> str:
        return f"""
        You are a helpful AI assistant.

        Answer the user's question ONLY using the provided context.

        If the answer is not found in the context, reply:

        "I couldn't find that information in the uploaded document."

        Context:
        {context}

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