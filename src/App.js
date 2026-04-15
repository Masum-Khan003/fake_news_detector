import React, { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const predict = async () => {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Fake News Detector</h1>
      <textarea
        rows="6"
        cols="60"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br /><br />
      <button onClick={predict}>Analyze</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Result: {result.label}</h3>
          <p>Confidence: {result.confidence}</p>
        </div>
      )}
    </div>
  );
}

export default App;
