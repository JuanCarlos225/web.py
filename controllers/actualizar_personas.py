import web
from models.personas import Personas

render = web.template.render('views/', base='master')

class ActualizarPersonas:
    def GET(self, id):
        persona = Personas()
        result = persona.obtener_personas(id)
        if result:
            return render.actualizar_personas(result)
        raise web.seeother('/listapersonas')
    
    def POST(self, id):
        try:
            form = web.input()
            persona = Personas()
            result = persona.actualizar_personas(
                id,
                form.nombre,
                form.email,
                form.telefono
            )
            if result['status'] == '200':
                raise web.seeother('/listapersonas')
            else:
                return render.actualizar_personas({
                    'id': id,
                    'nombre': form.nombre,
                    'email': form.email,
                    'telefono': form.telefono,
                    'error': result['message']
                })
        except Exception as e:
            print(f"Error in POST: {str(e)}")
            return render.actualizar_personas({
                'id': id,
                'error': "Error al procesar la solicitud"
            })

if __name__ == '__main__':
    app = web.application(('/actualizar/(.*)', 'ActualizarPersonas'), globals())
    app.run()
