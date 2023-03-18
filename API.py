# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import numpy as np
import warnings
warnings.filterwarnings("ignore", message="Trying to convert audio automatically from int32 to 16-bit int format")


API_KEY = "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"
openai.api_key = API_KEY


def speech_to_text(file_path):
    audio_file = open(file_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file, language='ar')

    print('You Say:')
    print("\"" + transcript['text'] + "\"")
    return transcript['text']


def generate_image(description):
    full_desc = 'give me logo with the following description: ' + description
    response = openai.Image.create(
        prompt=full_desc,
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url


def generate_code(description="Write a Python function that calculates the factorial of a number"):
    response = openai.Completion.create(engine="davinci-codex", prompt=description, max_tokens=1024)
    code = response.choices[0].text
    print(code)
    return code



class GPT():
    def __init__(self, defintion='You are a helpful assistant.'):
        self.messages = [{'role': 'system', 'content': defintion}]

    def ask_colors(self, new_message):
        user_text = '''
follow these conditions:
- your answer should only in json, don't say any word or comment.
- the format of the json you provide should be as following: 
{colors: [{red: <value>, green: <value>, blue: <value>, alpha: <values>}, ...]}
- before you answer translate the description provide to english to make your answer as good as possible.
- order the colors of the answer by their priority.
- you need specify a good colors schema based on some of famous theory, based the following description:\n
'''
        user_text += f'\"" + new_message + "\""'
        print('\ntext:\n' + user_text)
        gpt_answer = self.ask(user_text)
        return gpt_answer

    def ask_yon(self, new_message):
        user_text = '- translate the description message into english\n'
        user_text += "- answer the description as yes/no don't answer more than that, is the context of the description contain any kine of generation or creation for a website or webapplication?\n"
        user_text += "description:\n \"" + new_message + "\""
        print('\ntext:\n' + user_text)
        gpt_answer = self.ask(user_text)
        return gpt_answer

    def ask(self, new_message):
        self.messages.append({'role': 'user', 'content': new_message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )

        gpt_answer = response['choices'][0]['message']['content']
        self.messages.append({'role': 'assistant', 'content': gpt_answer})

        return gpt_answer


