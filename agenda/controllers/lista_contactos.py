import web

render = web.template.render('views/')

class Contactos: 
    def GET(self):
        return render.lista_contactos()