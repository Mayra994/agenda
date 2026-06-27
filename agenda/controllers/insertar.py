import web

render = web.template.render('views/')

class Insertar:
    def GET(self):
        return render.insertar()  