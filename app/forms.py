from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, TextAreaField


class FormLaporan(FlaskForm):
    inputDate = DateField()
    namaFile = StringField()
    judulLaporan = StringField()
    heading = StringField()
    isiLaporan = TextAreaField()
    submit = SubmitField()
