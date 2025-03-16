import web
from models.personas import Personas

render = web.template.render('views/', base='master')

class EliminarPersonas:
    def GET(self, id):
        try:
            persona = Personas()
            result = persona.eliminar_personas(id)
            web.seeother('/listapersonas')
        except Exception as e:
            print(f"Error al eliminar: {str(e)}")
            return "Error al eliminar persona"
