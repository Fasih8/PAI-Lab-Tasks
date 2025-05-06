from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based logic for demo
def chatbot_response(message):
    message = message.lower()
    if "admission" in message or "apply" in message:
        return "You can apply for admission on our official university portal. Applications are open from May to July."
    elif "courses" in message:
        return "We offer undergraduate and postgraduate programs in Engineering, Science, Business, and Arts."
    elif "deadline" in message:
        return "The deadline for admission applications is July 15th."
    elif "contact" in message or "email" in message:
        return "You can contact our admission office at admission@university.edu."
    else:
        return "I'm here to help with university admissions. Ask me about deadlines, courses, or how to apply!"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
