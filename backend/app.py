from flask import Flask, request, jsonify
from flask_cors import CORS
import text_to_speech
import task_execution

app = Flask(__name__)
CORS(app)

@app.route('/voice-command', methods=['POST'])
def voice_command():
    data = request.get_json()
    command = data.get('command')
    response = handle_command(command)
    text_to_speech.speak_text(response)
    return jsonify({'response': response})

def handle_command(command):
    if 'weather' in command:
        return task_execution.get_weather('New York')
    elif 'reminder' in command:
        return 'Reminder set!'
    elif 'message' in command:
        return 'Message sent!'
    else:
        return 'Command not recognized.'

if __name__ == '__main__':
    app.run(debug=True)
