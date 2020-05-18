from flask import Flask, render_template, request
import random 
import string

app = Flask(__name__)

def get_random(length=8):
    length=int(length)
    s_characters= '!$&?'
    characters = string.ascii_letters + string.digits + s_characters
    return ''.join((random.choice(characters) for i in range(length)))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method== 'POST':
        length=request.form.get('select_len')
        if length=='Choose':
            pw= get_random()
        else:
            pw=get_random(length)
        return render_template('index.html', pw=pw)
    return render_template('index.html', pw='')


if __name__ == '__main__':
    app.run()