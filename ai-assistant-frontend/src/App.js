import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');

  const handleVoiceCommand = async () => {
    try {
      const result = await axios.post('http://localhost:5000/voice-command', { command });
      setResponse(result.data.response);
    } catch (error) {
      console.error('Error processing voice command:', error);
    }
  };

  return (
    <div className="App">
      <h1>AI Personal Assistant</h1>
      <input
        type="text"
        value={command}
        onChange={(e) => setCommand(e.target.value)}
      />
      <button onClick={handleVoiceCommand}>Send Command</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default App;
