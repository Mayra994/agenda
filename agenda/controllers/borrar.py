import web

render = web.template.render('views/')

class Borrar:
    def GET(self):
        return render.borrar()  