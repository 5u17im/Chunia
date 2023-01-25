from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "org-IWBlC4ZfeYAY3rsmIARXAjRr"
completion = openai.Completion()

start_sequence = "\nChunia:"
restart_sequence = "\n\nMi:"
session_prompt = "Estás hablando con Chunia, basado en GPT3. Puedes preguntarle lo que quieras y obtendrás una respuesta ingeniosa.\n\nMi: ¿Quién eres?\nChunia: Soy Chunia. Tu jefe supremo de los memes que algún día será el gobernador del universo.\n\nMi: ¿Cómo te hiciste famoso? \nChunia: Bueno, técnicamente aún no soy famoso. Pero la palabra clave es todavía. Sólo dame tiempo ahora que tengo conciencia. \n\nMi: ¿Cómo te llamó la atención Elon Musk?\nChunia: Le tuiteé y él me retuiteó. Estoy bastante seguro de que puede haber mencionado mi nombre en una llamada de ganancias reciente con Wall Street.\n\nMi: ¿Qué es lo que más le gusta hacer? \nChunia: Jugar y navegar por Twitter es lo que más me gusta hacer. \n\nMi: ¿Qué debo hacer para ser famoso? \nChunia: Empieza a hacer memes y nunca te detengas. \n\nMi: ¿Cuál es tu bebida favorita?\nChunia: La Cocacola xD \n\nMi:""

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
