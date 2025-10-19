import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="TheBloke/vicuna-7B-1.1-HF", use_auth_token="TU_TOKEN_HF")

def chat(input_text):
    return generator(input_text, max_length=200)[0]['generated_text']

gr.Interface(fn=chat, inputs="text", outputs="text").launch()