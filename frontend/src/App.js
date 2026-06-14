// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from the Flask API endpoint
    fetch('http://localhost:5001/api/data')
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App" style={{ padding: '40px', fontFamily: 'Arial' }}>
      <header className="App-header">
        <h1>React + Flask Integration</h1>
        {loading ? (
          <p>Loading data from backend...</p>
        ) : data ? (
          <div>
            <p><strong>Backend Message:</strong> {data.message}</p>
            <p><strong>Status:</strong> {data.status}</p>
          </div>
        ) : (
          <p>Could not connect to the backend.</p>
        )}
      </header>
    </div>
  );
}

export default App;