import { useState } from "react";
import "./App.css";

import Upload from "./components/Upload";
import Chat from "./components/Chat";
import Answer from "./components/Answer";

function App() {
  const [answer, setAnswer] = useState(null);

  return (
    <div className="container">
      <header>
        <h1>🎓 EduRAG</h1>
        <p>AI University Document Assistant</p>
      </header>

      <Upload />

      <Chat onAnswer={setAnswer} />

      <Answer data={answer} />
    </div>
  );
}

export default App;