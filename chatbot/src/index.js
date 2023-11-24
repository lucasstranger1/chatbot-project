// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import Chatbot from './Chatbot';
import './index.css';


const root = document.getElementById('root');

ReactDOM.createRoot(root).render(
  <React.StrictMode>
    <Chatbot />
  </React.StrictMode>
);

// ... (rest of the file)
