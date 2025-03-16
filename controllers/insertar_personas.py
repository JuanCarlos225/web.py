import web
from models.personas import Personas

render = web.template.render('views/', base='master')

class InsertarPersonas:
    def GET(self):
        try:
            return render.insertar_personas()
        except Exception as error:
            print(f"Error: {error.args[0]}")
            return error.args[0]
    
    def POST(self):
        try:
            form = web.input()
            persona = Personas()
            response = persona.insertar_personas(form.nombre, form.email, form.telefono)
            web.seeother('/listapersonas')
        except Exception as error:
            print(f"Error: {error.args[0]}")
            return error.args[0]

