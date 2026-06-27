import web

render = web.template.render('views/')

class Editar:
    def GET(self):
        return render.editar() 