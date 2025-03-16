import web
from models.personas import Personas

render = web.template.render('views/', base='master')

class ListaPersonas:
    def GET(self):
        try:
            personas = Personas()
            resultado = personas.lista_personas()
            print("Datos obtenidos:", resultado)  # Para depuración
            return render.lista_personas(personas=resultado["personas"])
        except Exception as error:
            print(f"Error: {error.args[0]}")
            return render.lista_personas(personas={})






