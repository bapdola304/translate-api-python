from flask import Flask
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate/single/<q>')
def single_translate(q):
    result_text = translator.translate(q, dest='vi').text
    return {'result': result_text}