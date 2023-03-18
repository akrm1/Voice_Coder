import gradio as gr
from API import *
from Generator import generate_project

def logic(audio_path):
    gpt = GPT('you are an AI bot who answer yes/no for any intent of creation or making a web store or web application')

    user_text = speech_to_text(audio_path)
    image_url = generate_image(user_text)
    gpt_answer = gpt.ask_yon(user_text)

    website_url = 'http://127.0.0.1:7860'
    response = ''
    if 'yes' in gpt_answer.lower():
        response = generate_project() + ':\n' + website_url
    else:
        response = 'I am here to assist you for project, just make the motion'


    return image_url, response

def launch_ui():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                voice_input = gr.Audio(source="microphone", type='filepath')
                submit = gr.Button("Submit").style()
            with gr.Column():
                with gr.Accordion('Logo Generation'):
                    image_viewer = gr.Image(type="filepath")
                with gr.Accordion('Application URL'):
                    url = gr.Textbox(label="URL")
        with gr.Row():
            with gr.Column():
                pass
            with gr.Column():
                pass

        submit.click(fn=logic, inputs=[voice_input], outputs=[image_viewer, url])

    demo.launch()
