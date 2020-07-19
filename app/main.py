from flask import Flask
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/<text>')
def single_translate(text):
    text = translator.translate('hello', dest='vi').text
    return {'result': text}