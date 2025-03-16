import web
from controllers.index import Index
from controllers.lista_personas import ListaPersonas
from controllers.insertar_personas import InsertarPersonas
from controllers.detalle_personas import DetallePersonas
from controllers.actualizar_personas import ActualizarPersonas
from controllers.eliminar_personas import EliminarPersonas

urls = (
    '/', 'Index',
    '/listapersonas', 'ListaPersonas',
    '/insertarpersonas', 'InsertarPersonas',
    '/actualizarpersonas/(.*)', 'ActualizarPersonas',
    '/detallespersonas/(.*)', 'DetallePersonas',
    '/eliminarpersonas/(.*)', 'EliminarPersonas'
)

app = web.application(urls, globals())
render = web.template.render('views/', base='master')

if __name__ == "__main__":
    app.run()
