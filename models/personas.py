import pyrebase

config = {
    "apiKey": "AIzaSyAHyFssLhGMqdsJPLMvxsdT7adFxDXQa5c",
    "authDomain": "juan-demobd2.firebaseapp.com",
    "databaseURL": "https://juan-demobd2-default-rtdb.firebaseio.com",
    "storageBucket": "juan-demobd2.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Personas:
    def __init__(self):
        pass
    
    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            if personas.val() is None:
                return {
                    "status": "200",
                    "message": "No hay personas registradas",
                    "personas": {}
                }
            
            personas_dict = {}
            for key, persona in personas.val().items():
                personas_dict[key] = {
                    "id": key,
                    "nombre": persona.get('nombre', 'Unknown'),
                    "email": persona.get('email', 'N/A'),
                    "telefono": persona.get('telefono', 'N/A')
                }
            
            return {
                "status": "200",
                "message": "Personas consultadas correctamente",
                "personas": personas_dict
            }
        except Exception as error:
            print(f"Error: {error}")
            return {
                "status": "400",
                "message": "Error al consultar personas",
                "personas": {}
            }
        

    def insertar_personas(self, nombre, email, telefono):
        try:
            data = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            db.child("personas").push(data)
            response = {
                "status": "200",
                "message": "Persona insertada correctamente"
            }
            return response
        except Exception as error:
            print(f"Error: {error.args[0]}")
            response = {
                "status": "400",
                "message": "Error al insertar persona"
            }
            return response

    def obtener_personas(self, key):
        try:
            print(f"DEBUG: Buscando persona con key: {key}")
            persona = db.child("personas").child(key).get()
            if persona.val():
                data = persona.val()
                data['id'] = key

                if 'nombre' not in data: data['nombre'] = ''
                if 'email' not in data: data['email'] = ''
                if 'telefono' not in data: data['telefono'] = ''
                print(f"DEBUG: Persona encontrada: {data}")
                return data
            print("DEBUG: Persona no encontrada")
            return None
        except Exception as error:
            print(f"DEBUG: Error en obtener_persona: {str(error)}")
            return None

    def actualizar_personas(self, key, nombre, email, telefono):
        try:
            if not all([nombre, email, telefono]):
                return {
                    "status": "400",
                    "message": "Todos los campos son requeridos"
                }
            
            # Verificar si la persona existe
            persona_actual = self.obtener_personas(key)
            if not persona_actual:
                return {
                    "status": "404",
                    "message": "Persona no encontrada"
                }
            
            data = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            db.child("personas").child(key).update(data)
            return {
                "status": "200",
                "message": "Persona actualizada correctamente"
            }
        except Exception as error:
            print(f"DEBUG: Error en actualización: {str(error)}")
            return {
                "status": "400",
                "message": "Error al actualizar persona"
            }

    def eliminar_personas(self, key):
        try:
            # Verificar si la persona existe
            persona = self.obtener_personas(key)
            if not persona:
                return {
                    "status": "404",
                    "message": "Persona no encontrada"
                }
            
            # Eliminar la persona
            db.child("personas").child(key).remove()
            return {
                "status": "200",
                "message": "Persona eliminada correctamente"
            }
        except Exception as error:
            print(f"DEBUG: Error en eliminación: {str(error)}")
            return {
                "status": "400",
                "message": "Error al eliminar persona"
            }

#persona = Personas()
#print(persona.lista_personas())

