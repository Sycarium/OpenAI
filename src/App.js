import React from 'react';
import './App.css';
import ChatbotComponent from './ReactOpenAI.js';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>My Chatbot App</h1>
      </header>
      <ChatbotComponent />
    </div>
  );
}

export default App;