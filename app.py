from flask import abort, Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/v2')
def index_v2():
    return render_template('index_v2.html')


@app.route('/v3')
def index_v3():
    return render_template('index_v3.html')


@app.route('/login_v2', methods=('POST',))
def login_v2():
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

    if 'error-codes' in json_resp:
        abort(400)

    if not json_resp['success']:
        return render_template('failure.html')

    return render_template('success.html')


@app.route('/login_v3', methods=('POST',))
def login_v3():
    app.logger.info('Login!')
    app.logger.info(request)

    username = request.form['username']
    password = request.form['password']
    recaptcha_response = request.form['g-recaptcha-response']

    body = {
        'secret': '6LdKbpsUAAAAAInacIxQ4BHV8zUjk8k6y0TM9OGM',
        'response': recaptcha_response
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=body)

    json_resp = response.json()

    if 'error-codes' in json_resp:
        abort(400)

    if json_resp['score'] < 0.5:
        return render_template('failure.html')

    return render_template('success.html')


@app.route('/validate_captcha_v2', methods=('POST',))
def validate_captcha_v2():
    recaptcha_response = request.form['g-recaptcha-response']

    body = {
        'secret': '6LfqYJoUAAAAAPSdj_baC4iRJEcttVfpYnyJpNyB',
        'response': recaptcha_response
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=body)

    json_resp = response.json()

    if 'error-codes' in json_resp:
        abort(400)

    if not json_resp['success']:
        return render_template('failure.html')

    return render_template('success.html')


@app.route('/validate_captcha_v3', methods=('POST',))
def validate_captcha_v3():
    recaptcha_response = request.form['g-recaptcha-response']

    body = {
        'secret': '6LdKbpsUAAAAAInacIxQ4BHV8zUjk8k6y0TM9OGM',
        'response': recaptcha_response
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=body)

    json_resp = response.json()

    if 'error-codes' in json_resp:
        abort(400)

    if json_resp['score'] < 0.5:
        return render_template('failure.html')

    return render_template('success.html')
