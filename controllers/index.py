import web

render = web.template.render('views/', base='master')

class Index:
    def GET(self):
        
        try:
            return render.index()
        except Exception as error:
            print(f"Error: {error.args[0]}")
            return error.args[0]
