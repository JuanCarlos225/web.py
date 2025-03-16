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
            response = {
                "status": "200",
                "message": "Personas consultadas correctamente",
                "personas": dict(personas.val())
            }
            return response
        except Exception as error:
            print(f"Error: {error.args[0]}")
            response = {
                "status": "400",
                "message": "Error al consultar personas"
            }
            return response
        
        


#persona = Personas()
#print(persona.lista_personas()) 

