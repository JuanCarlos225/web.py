import web
from models.personas import Personas

render = web.template.render('views/', base='master')

class DetallePersonas:
    def GET(self, key):
        try:
            print(f"DEBUG: Accediendo a detalles con key: {key}")  # Debug print
            if not key:
                print("DEBUG: Key no proporcionada")
                return web.seeother('/listapersonas')

            persona_model = Personas()
            persona = persona_model.obtener_personas(key)  # Changed from obtener_persona to obtener_personas
            
            if persona:
                print(f"DEBUG: Persona encontrada: {persona}")  # Debug print
                return render.detalle_personas(persona=persona, key=key)
            else:
                print(f"DEBUG: Persona no encontrada para key: {key}")  # Debug print
                return web.seeother('/listapersonas')
                
        except Exception as error:
            print(f"DEBUG: Error en detalle: {str(error)}")  # Debug print
            return web.seeother('/listapersonas')
