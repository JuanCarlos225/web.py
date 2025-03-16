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
            # Crear la respuesta incluyendo el ID
            response = {
                "status": "200",
                "message": "Personas consultadas correctamente",
                "personas": []
            }
            for id_persona, info in personas.val().items():
                info_with_id = {
                    "id": id_persona,
                    "nombre": info.get('nombre', 'Unknown'),  # Nombre por defecto
                    "telefono": info.get('telefono', None)  # Teléfono si existe
                }
                response['personas'].append(info_with_id)
            return response
        except Exception as error:
            print(f"Error: {error}")
            return {
                "status": "400",
                "message": "Error al consultar personas"
            }
        