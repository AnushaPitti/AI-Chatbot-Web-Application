# AI Chatbot Web Application

## Project Overview
An AI-powered chatbot web application built with HTML, CSS, Flask, and basic Machine Learning concepts.

## Features

### Mandatory Features
- Welcome Page
- Chat Interface
- User Message Input
- AI Response Generation
- Flask Backend Integration
- Dynamic Chat Display
- Attractive User Interface
- Multiple User Queries Handling

### Optional Features (All Implemented)
- Voice Input (Web Speech API)
- Dark Mode
- Login System
- Chat History
- Real-Time Responses (Typing indicator)
- AI API Integration (Pattern matching + Similarity scoring)
- Responsive Design

## How to Run
1. Make sure Python 3.8+ is installed
2. Install Flask: pip install flask
3. Navigate to the project folder: cd AI_Chatbot
4. Run: python app.py
5. Open browser: http://localhost:5000

## Login Credentials
- admin / admin123
- anusha / pass123
- user / user123
- Or register a new account
- Or continue as Guest

## Project Structure
AI_Chatbot/
    app.py          - Flask backend server
    chatbot.py      - ChatBot class with ML logic
    responses.json  - Knowledge base
    templates/
        index.html  - Frontend interface
    static/
        style.css   - Styling and themes
    README.md       - Project documentation

## Technologies Used
- Python 3
- Flask (Web Framework)
- HTML5, CSS3, JavaScript
- Web Speech API (Voice Input)
- difflib.SequenceMatcher (ML - String Similarity)
