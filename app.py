from flask import abort, Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=('POST',))
def login():
    app.logger.info('Login!')
    app.logger.info(request)

    username = request.form['username']
    password = request.form['password']
    recaptcha_response = request.form['g-recaptcha-response']

    body = {
        'secret': '6LfqYJoUAAAAAPSdj_baC4iRJEcttVfpYnyJpNyB',
        'response': recaptcha_response
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=body)

    json_resp = response.json()

    if not json_resp['success']:
        abort(400)

    return render_template('sucess.html')


@app.route('/validate_captcha', methods=('POST',))
def validate_captcha():
    recaptcha_response = request.form['g-recaptcha-response']

    body = {
        'secret': '6LfqYJoUAAAAAPSdj_baC4iRJEcttVfpYnyJpNyB',
        'response': recaptcha_response
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=body)

    json_resp = response.json()

    if not json_resp['success']:
        abort(400)

    return render_template('sucess.html')
