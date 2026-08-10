import "./App.css";
import Upload from "./components/Upload";

function App() {
  return (
    <div className="container">

      <header>
        <h1>🎓 EduRAG</h1>
        <p>AI University Document Assistant</p>
      </header>

      <Upload />

    </div>
  );
}

export default App;