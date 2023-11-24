# ASD-Q&A Chatbot

ASD-Q&A Chatbot is a simple chatbot interface that allows users to interact with a question and answer system. The chatbot is designed to provide information based on categories, questions, and answers.


<img src="https://github.com/lucasstranger1/chatbot-project/blob/main/Chatbot-interface.png" alt="Chatbot Interface" width="300" height="600">



## Features

- **Category Selection:** Users can select a category to view related questions.
- **Question Selection:** Upon selecting a category, users can choose a specific question.
- **Answer Display:** The chatbot displays answers corresponding to the selected question.
- **User Interaction:** Users can input messages to the chatbot, and it responds accordingly.
- **Greeting Response:** The chatbot provides a greeting response when users send greetings.

## Technologies Used

- **React:** The chatbot interface is built using the React library.
- **Axios:** Axios is used for making asynchronous HTTP requests to fetch data.
- **CSS:** Custom styling is applied using CSS for a visually appealing interface.

## Backend and API Data Conversion

### Django Backend

The ASD-Q&A Chatbot's backend is built using Django, which serves as the framework handling data management and conversion into API JSON files. 

### Data Conversion into API JSON

The Django backend processes and organizes the provided data into structured formats compatible with the frontend. Through Django's models and views, the application transforms the categorized questions and answers into accessible API endpoints that the frontend can efficiently consume.

For instance, Django models are used to define the data structure, while views handle the logic to serialize this data into JSON format, making it accessible via API endpoints.

These endpoints, when accessed by the frontend, provide the necessary data for category selection, question retrieval, and answer display within the chatbot interface.

## Getting Started

To run the ASD-Q&A Chatbot locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/lucasstranger1/chatbot-project.git
2. Navigate to the project directory:
    cd asd-qna-chatbot
3. Install dependencies:
    npm install
4. Start the development server:
    npm start
5. Open your browser and visit http://localhost:3000 to interact with the chatbot.

Usage
    Select a category from the list to explore related questions.
    Choose a specific question to view corresponding answers.
    Input messages in the text box to interact with the chatbot.
    Contributing
    If you'd like to contribute to ASD-Q&A Chatbot, please follow these guidelines:

    1. Fork the repository.
    2. Create a new branch for your feature or bug fix.
    3. Commit your changes with descriptive commit messages.
    4. Push your changes to your fork.
    5. Submit a pull request.
    
    License
    
    This project is licensed under the MIT License - see the LICENSE file for details.

    Feel free to customize this README file based on your project's specific details and requirements.
