// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import Chatbot from './Chatbot';
import './index.css';
import reportWebVitals from './reportWebVitals';

const root = document.getElementById('root');

ReactDOM.createRoot(root).render(
  <React.StrictMode>
    <Chatbot />
  </React.StrictMode>
);

// ... (rest of the file)
