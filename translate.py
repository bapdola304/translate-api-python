from flask import Flask
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate/single/<text>')
def single_translate(text):
    text = translator.translate(text, dest='vi').text
    return {'result': text}
 
if __name__ == '__main__':
    app.run()