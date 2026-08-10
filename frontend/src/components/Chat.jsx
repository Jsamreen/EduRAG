import { useState } from "react";
import api from "../../api/api";

function Chat({ onAnswer }) {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    try {
      setLoading(true);

      const response = await api.post("/chat", {
        question,
      });

      onAnswer(response.data);
      setQuestion("");
    } catch (error) {
      console.error("Chat error:", error);
      alert("Could not get an answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Ask EduRAG</h2>

      <div className="question-row">
        <input
          type="text"
          placeholder="Ask a question about your documents..."
          value={question}
          disabled={loading}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              askQuestion();
            }
          }}
        />

        <button
          onClick={askQuestion}
          disabled={loading}
        >
          {loading ? "Thinking..." : "Ask AI"}
        </button>
      </div>

      {loading && (
        <div className="thinking-loader">
          <div className="student">👩‍🎓</div>

          <div className="book-animation">
            📖
          </div>

          <div className="thinking-text">
            EduRAG is reading your documents
            <span className="dots">
              <span>.</span>
              <span>.</span>
              <span>.</span>
            </span>
          </div>
        </div>
      )}
    </div>
  );
}

export default Chat;