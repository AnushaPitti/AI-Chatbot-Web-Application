# 🤖 AI Chatbot Web Application

An AI-powered chatbot web application built with **Flask, HTML, CSS, JavaScript**, and basic **Machine Learning** concepts. This chatbot interacts with users through a modern web interface, accepts messages, and generates intelligent responses dynamically.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Login Credentials](#-login-credentials)
- [Screenshots](#-screenshots)
- [Sample Output](#-sample-output)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Project Overview

The AI Chatbot is a simple yet powerful web-based application developed using **HTML, CSS, Flask**, and basic **Machine Learning** concepts. The chatbot:

- Interacts with users through a beautiful chat interface
- Accepts user messages and processes input
- Generates automated responses dynamically using **pattern matching** and **string similarity scoring**
- Behaves like a basic AI assistant communicating through a web browser

---

## ✨ Features

### ✅ Mandatory Features

| # | Feature | Description | Status |
|---|---------|-------------|--------|
| 1 | **Welcome Page** | Beautiful landing page with login/register options | ✅ Done |
| 2 | **Chat Interface** | Clean, modern chat UI with message bubbles | ✅ Done |
| 3 | **User Message Input** | Text input with send button and Enter key support | ✅ Done |
| 4 | **AI Response Generation** | ML-based pattern matching + similarity scoring | ✅ Done |
| 5 | **Flask Backend Integration** | Full Flask server with REST API endpoints | ✅ Done |
| 6 | **Dynamic Chat Display** | Real-time message rendering with animations | ✅ Done |
| 7 | **Attractive User Interface** | Modern design with gradients, shadows, animations | ✅ Done |
| 8 | **Multiple User Queries** | Handles unlimited conversation topics | ✅ Done |

### 🌟 Optional Features (All Implemented!)

| # | Feature | Description | Status |
|---|---------|-------------|--------|
| 1 | **🎤 Voice Input** | Speech-to-text using Web Speech API | ✅ Done |
| 2 | **🌙 Dark Mode** | Toggle between light and dark themes | ✅ Done |
| 3 | **🔐 Login System** | User authentication with login/register/guest | ✅ Done |
| 4 | **📜 Chat History** | Sidebar with full conversation history | ✅ Done |
| 5 | **⚡ Real-Time Responses** | Typing indicator animation before bot replies | ✅ Done |
| 6 | **🤖 AI API Integration** | Pattern matching + SequenceMatcher ML algorithm | ✅ Done |
| 7 | **📱 Responsive Design** | Works on desktop, tablet, and mobile screens | ✅ Done |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Backend programming language |
| **Flask 3.1** | Web framework for backend server |
| **HTML5** | Page structure and content |
| **CSS3** | Styling, animations, dark mode, responsive design |
| **JavaScript** | Frontend interactivity and API calls |
| **difflib (SequenceMatcher)** | ML - String similarity scoring for smart responses |
| **Web Speech API** | Browser-based voice input recognition |

---

## 📁 Project Structure

```
AI_Chatbot/
│
├── app.py                 # Flask backend server with all routes
├── chatbot.py             # ChatBot class with ML-based response logic
├── responses.json         # Knowledge base with patterns and responses
│
├── templates/
│   └── index.html         # Frontend - Complete UI with all features
│
├── static/
│   └── style.css          # Styling - Dark mode, responsive, animations
│
└── README.md              # Project documentation (this file)
```

### File Descriptions

| File | Lines | Description |
|------|-------|-------------|
| `app.py` | ~90 | Flask server with routes: login, register, logout, chat, history |
| `chatbot.py` | ~40 | ChatBot class using pattern matching + SequenceMatcher |
| `responses.json` | ~130 | 16 categories of responses (greetings, AI, ML, Python, etc.) |
| `index.html` | ~280 | Complete frontend with login, chat, voice, history sidebar |
| `style.css` | ~450 | Full styling with CSS variables, dark theme, responsive breakpoints |

---

## 🚀 How to Run

### Prerequisites
- **Python 3.8** or higher installed
- **pip** (Python package manager)

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/AI-Chatbot-Web-Application.git

# 2. Navigate to project folder
cd AI-Chatbot-Web-Application

# 3. Install dependencies
pip install flask

# 4. Run the application
python app.py
```

### Expected Output
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
```

### Open in Browser
```
http://localhost:5000
```

---

## 🔐 Login Credentials

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin123` | Admin User |
| `anusha` | `pass123` | Regular User |
| `user` | `user123` | Regular User |

> 💡 You can also **Register** a new account or click **Continue as Guest** to skip login.

---

## 📸 Screenshots

### 🏠 Welcome / Login Page
![Welcome Page](screenshots/welcome.png)

### 💬 Chat Interface (Light Mode)
![Chat Light](screenshots/chat-light.png)

### 🌙 Chat Interface (Dark Mode)
![Chat Dark](screenshots/chat-dark.png)

### 🎤 Voice Input
![Voice Input](screenshots/voice-input.png)

### 📜 Chat History Sidebar
![Chat History](screenshots/chat-history.png)

### 📱 Mobile Responsive View
![Mobile View](screenshots/mobile-view.png)

> 📝 **Note:** To add screenshots, create a `screenshots/` folder in your repository and upload images.

---

## 💬 Sample Output

```
Welcome to AI Chatbot

User: Hello
Bot: Hi! How can I help you today?

User: What is Machine Learning?
Bot: Machine Learning is a branch of AI that allows systems to learn 
     from data and improve from experience without being explicitly programmed.

User: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

User: What is Flask?
Bot: Flask is a lightweight Python web framework used to build web 
     applications quickly and easily.

User: Bye
Bot: Goodbye! Have a great day!
```

---

## 🧠 How the AI Works

The chatbot uses a combination of two techniques:

### 1. Pattern Matching
- User input is compared against predefined patterns in `responses.json`
- If a pattern is found as a substring in the user's message, the corresponding response is returned

### 2. String Similarity Scoring (Machine Learning)
- Uses Python's `difflib.SequenceMatcher` algorithm
- Calculates similarity ratio between user input and all known patterns
- If similarity score > 0.5 (50%), the best matching response is returned
- Otherwise, a default response is given

```python
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

# Example: similarity("what is ml", "what is machine learning") = 0.65
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve the main page |
| `POST` | `/login` | User authentication |
| `POST` | `/register` | New user registration |
| `POST` | `/logout` | User logout |
| `POST` | `/chat` | Send message & get bot response |
| `GET` | `/history` | Get chat history for logged-in user |
| `POST` | `/clear_history` | Clear chat history |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m "Add your feature"`
4. **Push** to the branch: `git push origin feature/your-feature`
5. **Open** a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Pitti Anusha**
- Internship Project at Think Champ PV LTD
- Associate Instrumentation Engineer

---

<p align="center">
  Made with ❤️ using Python & Flask
</p>
