from flask import render_template,url_for,\
                redirect,flash,request,g,jsonify, current_app

from flask_babel import _, get_locale
from app.models import Post
from app.translate import translate
from app.main.forms import PostForm

from app.main import bp

@bp.before_request
def before_request():
    g.locale = str(get_locale())

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    return render_template(
        'main/index.html',
        title=_('Home'),
        res=1)

@bp.route('/translate', methods=['POST'])
def translate_text():
    return jsonify({
        'text':
        translate(request.form['text'], request.form['source_language'],
                  request.form['dest_language'])
    })
