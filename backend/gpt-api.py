import openai

openai.api_key = 'your_openai_api_key'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def handle_command(command):
    if 'weather' in command:
        return task_execution.get_weather('New York')
    elif 'reminder' in command:
        return 'Reminder set!'
    elif 'message' in command:
        return 'Message sent!'
    else:
        return get_chatgpt_response(command)
