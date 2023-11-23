// src/Chatbot.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Chatbot.css'; // Import the CSS file

const Chatbot = () => {
const [categories, setCategories] = useState([]);
const [selectedCategory, setSelectedCategory] = useState(null);
const [questions, setQuestions] = useState([]);
const [selectedQuestion, setSelectedQuestion] = useState(null);
const [answers, setAnswers] = useState([]);
const [userInput, setUserInput] = useState('');

useEffect(() => {
// Fetch categories on component mount
const fetchCategories = async () => {
    try {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/categories/');
    setCategories(response.data);
    } catch (error) {
    console.error('Error fetching categories:', error);
    }
};

fetchCategories();
}, []);

const handleCategorySelect = async (categoryId) => {
// Fetch questions based on selected category
try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/questions/?category=${categoryId}`);
    setQuestions(response.data);
    setSelectedCategory(categoryId);
    setSelectedQuestion(null); // Reset selected question when category changes
    setAnswers([]); // Reset answers when category changes
} catch (error) {
    console.error('Error fetching questions:', error);
}
};

const handleQuestionSelect = async (questionId) => {
// Fetch answers based on selected question
try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/answers/?question=${questionId}`);
    setAnswers(response.data);
    setSelectedQuestion(questionId);
} catch (error) {
    console.error('Error fetching answers:', error);
}
};

const handleUserInput = (event) => {
setUserInput(event.target.value);
};

const handleSendMessage = () => {
// Check if the user's message is a greeting
const greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'];

if (greetings.includes(userInput.toLowerCase())) {
    // If the user's message is a greeting, respond with a greeting feedback
    const randomGreetingResponse = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!', 'Good day!'];
    const randomIndex = Math.floor(Math.random() * randomGreetingResponse.length);
    const botResponse = randomGreetingResponse[randomIndex];

    // Update the answers state with the greeting response
    setAnswers([{ id: Date.now(), answer_text: botResponse }]);
} else {
    // If the user's message is not a greeting, send the message to the server (you can add this logic based on your requirements)
    console.log('Sending message:', userInput);
    // Clear the input box after sending
    setUserInput('');
}
};

return (
<div className="container">
    <h1>Chatbot Interface</h1>
    <div>
    <p>Select a category:</p>
    <ul>
        {categories.map((category) => (
        <li key={category.id} onClick={() => handleCategorySelect(category.id)}>
            {category.name}
        </li>
        ))}
    </ul>
    </div>
    {selectedCategory && (
    <div>
        <h2>Questions in {categories.find((cat) => cat.id === selectedCategory)?.name}</h2>
        <ul>
        {questions.map((question) => (
            <li key={question.id} onClick={() => handleQuestionSelect(question.id)}>
            {question.question_text}
            </li>
        ))}
        </ul>
    </div>
    )}
    {selectedQuestion && (
    <div>
        <h2>Answers for the selected question:</h2>
        <ul>
        {answers.map((answer) => (
            <li key={answer.id}>{answer.answer_text}</li>
        ))}
        </ul>
    </div>
    )}
    <div id="input-section">
    <input
        type="text"
        placeholder="Type a message"
        value={userInput}
        onChange={handleUserInput}
    />
    <button className="send" onClick={handleSendMessage}>
        <div className="circle">
        <i className="zmdi zmdi-mail-send"></i>
        </div>
    </button>
    </div>
</div>
);
};

export default Chatbot;
