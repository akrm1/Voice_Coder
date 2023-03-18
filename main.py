import gradio as gr
from gradio.components import Image
from API import *
from Project import *
from App import *
from UI import *



def whisper_gpt_example(audio_path):
    gpt = GPT('''
you are an AI bot who answer with a json file of list of colors based on some
theory schema with the following format {colors: [{red: <value>, green: <value>, blue: <value>, alpha: <values>}
for any intent of creation or making a web store or web application, and i am a robot only understand json!
    ''')

    user_text = speech_to_text(audio_path)
    gpt_answer = gpt.ask(user_text)

    return gpt_answer

def dalle_example(description):
    image_url = generate_image(description)
    return image_url

#i want the latest engine for codex?
def generate_code_example(audio_path):
    user_text = speech_to_text(audio_path)
    code = generate_code(user_text)
    return code

#demo = gr.Interface(fn=whisper_gpt_example, inputs=gr.Audio(source="microphone", type='filepath'), outputs="text")
#demo = gr.Interface(fn=dalle_example, inputs='text', outputs=Image(type="filepath"))
#demo.launch()



launch_ui()

















