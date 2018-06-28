from flask import Flask
from flask import render_template, url_for, request, g, jsonify, abort
from config import Config
from flask_bootstrap import Bootstrap
from flask_babel import _,Babel

app = Flask(__name__)

app.config.from_object(Config)
bootstrap = Bootstrap()
babel = Babel()
bootstrap.init_app(app)
babel.init_app(app)



etarget = []
etemp = True
enow = 1
emax = 999


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')


@app.route('/start', methods=['POST'])
def start():
    try:
        cat = int(request.form['floors'])
    except TypeError:
        abort(400, 'Please input correct integer value.')
    except ValueError:
        cat = 5
    cat = 5 if cat < 0 else 30 if cat > 50 else cat

    enow, emax = 1, cat

    return jsonify({'floor': cat})


@app.route('/running', methods=['POST'])
def run():
    key = int(request.form['etarget'])
    if key not in range(1, emax + 1):
        abort(404)
    if not len(etarget) or key not in etarget:
        ctx = app.app_context()
        etarget.append(key)
        ctx.push()
        print(emax)
    return jsonify({'enow': enow})


@app.route('/moving', methods=['POST'])
def move():
    elast = enow
    print("now{},etarget{}".format(emax, etarget))
    if int(request.form['move']) == 1 and len(etarget):
        enow += 0 if enow == etarget[
            -1] else 1 if enow < etarget[-1] else -1
        if (enow == etarget[-1]):
            etarget.pop()
    app.app_context().push()
    return jsonify({'enow': enow, 'elast': elast})
