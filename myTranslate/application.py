from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Required, length
from googletrans import Translator
import googletrans

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = '5sNFu6ESrWE9bBYpkr8XbPiqiZ1qCmA6'

Bootstrap(app)
languages = [' ' ] + [googletrans.LANGUAGES[i].capitalize() for i in googletrans.LANGUAGES]

class TranslateText(FlaskForm):
    text= TextAreaField('Enter text to translate: ', validators=[DataRequired(), length(max=1000)], default=None)
    lang = SelectField(u'Language to translate to', choices = (languages), validators = [Required()])
    submit = SubmitField('Translate')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TranslateText()
    message = "This is where your translated text will show"
    translator = Translator()
    result = ''
    if form.validate_on_submit():
        text = form.text.data
        lang = form.lang.data
        result = translator.translate(text, dest=lang)
    return render_template('index.html', form=form, message=message, result=result)
