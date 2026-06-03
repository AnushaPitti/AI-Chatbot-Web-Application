from flask import Flask, render_template, request, jsonify, session
from chatbot import ChatBot
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'ai_chatbot_secret_key_2026'

chatbot = ChatBot()

# Simple user database
users_db = {
    'admin': 'admin123',
    'anusha': 'pass123',
    'user': 'user123'
}

# Chat history storage
chat_histories = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if username in users_db and users_db[username] == password:
        session['user'] = username
        if username not in chat_histories:
            chat_histories[username] = []
        return jsonify({'success': True, 'username': username})
    return jsonify({'success': False, 'message': 'Invalid username or password!'})


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'success': True})


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password required!'})
    if username in users_db:
        return jsonify({'success': False, 'message': 'Username already exists!'})

    users_db[username] = password
    chat_histories[username] = []
    session['user'] = username
    return jsonify({'success': True, 'username': username})


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    bot_response = chatbot.get_response(user_message)
    timestamp = datetime.now().strftime('%H:%M')

    user = session.get('user')
    if user and user in chat_histories:
        chat_histories[user].append({
            'user': user_message,
            'bot': bot_response,
            'time': timestamp
        })

    return jsonify({
        'response': bot_response,
        'time': timestamp
    })


@app.route('/history', methods=['GET'])
def get_history():
    user = session.get('user')
    if user and user in chat_histories:
        return jsonify({'history': chat_histories[user]})
    return jsonify({'history': []})


@app.route('/clear_history', methods=['POST'])
def clear_history():
    user = session.get('user')
    if user and user in chat_histories:
        chat_histories[user] = []
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
