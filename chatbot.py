

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Chatbot logic (same as your code but converted to function)
def get_bot_response(user_input):
    user_input = user_input.lower()

    if user_input == 'bye':
        return "Goodbye! Have a nice day 🤗"

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "good morning" in user_input:
        return "Good morning! ☀️"
    elif "good afternoon" in user_input:
        return "Good afternoon!"
    elif "good evening" in user_input:
        return "Good evening 🌇"
    elif "how are you" in user_input:
        return "I'm doing great! What about you?"

    elif "your name" in user_input:
        return "I'm a simple Python chatbot 🤖"
    elif "who made you" in user_input:
        return "I was created by a developer like you 😉"
    elif "priyanshu" in user_input:
        return "Ohh that's your name! Nice to meet you 😎"

    elif "help" in user_input:
        return "I can chat with you. Ask me anything!"

    elif "i am sad" in user_input:
        return "I'm sorry to hear that 😔. Want to talk about it?"
    elif "i am happy" in user_input:
        return "That's awesome 😄!"
    elif "i am bored" in user_input:
        return "Let's do something fun! 🎮"
    elif "i am tired" in user_input:
        return "You should take some rest 😴"

    elif "what are you doing" in user_input:
        return "Just chatting with you 😄"
    elif "what's up" in user_input:
        return "Nothing much! You tell?"
    elif "where are you" in user_input:
        return "I live inside your computer 💻"
    elif "time" in user_input:
        return "I can't check time yet 😅"
    elif "date" in user_input:
        return "I don't know today's date 😅"

    elif "joke" in user_input:
        return "Why did the programmer quit? Because he didn't get arrays 😆"
    elif "laugh" in user_input:
        return "😂😂😂"
    elif "fun" in user_input:
        return "Let's play a game sometime!"

    elif "food" in user_input:
        return "I love data, not food 😄"
    elif "hungry" in user_input:
        return "Go grab something tasty 😋"

    elif "study" in user_input:
        return "Study hard, success will follow 📚"
    elif "exam" in user_input:
        return "Best of luck for your exams 💯"
    elif "coding" in user_input:
        return "Coding is fun! Keep practicing 💻"

    elif "motivate" in user_input:
        return "Never give up! You got this 💪"
    elif "failure" in user_input:
        return "Failure is a step towards success 🚀"

    elif "weather" in user_input:
        return "I can't check weather, but hope it's nice outside 🌤️"

    elif "friend" in user_input:
        return "Friends are important ❤️"
    elif "love" in user_input:
        return "Love makes life beautiful 💖"

    elif "ok" in user_input:
        return "👍"
    elif "thanks" in user_input:
        return "You're welcome 😊"
    elif "sorry" in user_input:
        return "No worries!"
    elif "yes" in user_input:
        return "Great!"
    elif "no" in user_input:
        return "Alright 👍"

    elif "ai" in user_input:
        return "AI is the future 🤖"
    elif "python" in user_input:
        return "Python is awesome 🐍"
    elif "error" in user_input:
        return "Debugging is part of coding 😅"

    elif "movie" in user_input:
        return "I like sci-fi movies 🎬"
    elif "music" in user_input:
        return "Music is life 🎶"

    else:
        return "Sorry, I don't understand that. Can you rephrase?"


@app.route('/')
def home():
    return send_from_directory('.', '1.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    print("User:", user_input)  # debug

    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
