from flask import Flask, render_template, request, url_for, flash
from forms import DocForm, CSRFProtect
from dataclasses import dataclass
from docx import Document
import datetime
import shutil

#IDEA TO IMPLEMENT UNTIL NEXT SEMESTER
#ADD A DICTIONARY SO I DONT HAVE TO INPUT BOTH THE CLASS AND THE PROFESOR SO IT GETS BOTH BY JUST INPUTING THE CLASS NAME
#FIXING THE FLASH THING ONCE I LEARN HOW TO IMPLEMENT IT CORRECTLY


def file_name(assign: str, act: str) -> str:
    a = ''.join([ s[0] for s in assign.split() ])
    file = f'{a} Act{act}'
    return file

@dataclass
class Data():
    def __init__(self, name, id, assignature, professor, module, activity) -> None:
        self.name = name
        self.id =  id
        self.assignature = assignature
        self.professor = professor
        self.module = module
        self.activity = activity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0fb9fa65ac5c694ab146904833ce521'

#creacion de la llave csrf
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def get_info():

    #la parte divertida, checar los errores del forms
    #print(form.errors)
    form = DocForm(request.form)
    
    if form.validate():

        name = request.form['name']
        id = request.form['id']
        assignature =request.form['assignature']
        professor = request.form['professor']
        module = request.form['module']
        activity = request.form['activity']
        date = datetime.datetime.now()
        
        document = Document()

        table = document.add_table(rows=5, cols=2)
        row_cells = table.rows[0].cells
        row_cells[0].text = f'Nombre:\n{name}'
        row_cells[1].text = f'Matricula:\n{id}'
        row_cells = table.add_row().cells
        row_cells[0].text = f'Nombre del Curso: \n{assignature}'
        row_cells[1].text = f'Nombre del profesor:\n{professor}'
        row_cells = table.add_row().cells
        row_cells[0].text = f'Modulo:\n{module}'
        row_cells[1].text = f'Actividad:\n{activity}'
        row_cells = table.add_row().cells
        row_cells[0].text = f'Fecha: {date.strftime("%x")}'
        row_cells = table.add_row().cells
        row_cells[0].text = f'Bibliografía: '
        
        file = f'{file_name(assignature, activity)}.docx'
        try:
            #flashing to know it was validated
            flash('Document created succesfully', 'succes')

            document.save(file)
            shutil.move(f'C:\\Users\\Dell\\OneDrive\\Desktop\\DocManager\\{file}', 'C:\\Users\\Dell\\OneDrive\\Desktop\\Tecmi')
        except Exception as e:
            flash('Unable to create document', 'succes')

    

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)