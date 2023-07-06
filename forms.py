from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired


class DocForm(FlaskForm):
    name = StringField('Name', 
                          validators=[DataRequired()])
    
    id = StringField('Id', 
                          validators=[DataRequired()])
    
    assignature = StringField('Assignature', 
                          validators=[DataRequired()])
    
    professor = StringField('Professor', 
                          validators=[DataRequired()])
    
    module = StringField('Module', 
                          validators=[DataRequired()])
    
    activity = StringField('Activity', 
                          validators=[DataRequired()])
    
    submit = SubmitField('Submit')
    

