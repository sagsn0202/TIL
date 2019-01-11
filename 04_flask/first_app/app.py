from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/ssafy')
def ssafy():
    return 'ssafy'

@app.route('/lotto')
def pick_lotto():
    lotto_numbers = random.sample(range(1, 46), 6)
    return jsonify(lotto_numbers)

# < > variable routing
@app.route('/hi/<string:name>')
def hi(name):
    return(f'Hi! {name}')

@app.route('/dictionary/<string:word>')
def dictionary(word):
    words_dict = { 'apple': '사과' }
    if word in words_dict:
        return f'{word}은(는) {words_dict[word]}'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다.'

if __name__ == '__main__':
    app.run(debug=True)
    # 혹은 export FLASK_ENV='development' ; bash ; reset
    # 밖에서 부르기 위해서는 $FLASK_ENV
    # export RUN_FLASK='python app.py'
    # $RUN_FLASK로 환경변수 호출(alias와 구분하자.)
    # export RUN_FLASK= 변수 초기화