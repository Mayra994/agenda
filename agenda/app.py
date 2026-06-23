import web  
urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
    '/ver', 'Ver',
    '/editar','Editar',
    '/borrar','Borrar',
    '/insertar','Insertar'
)

app = web.application(urls, globals())
render = web.template.render('views/')

class Index:
    def GET(self):
        return render.index()

class Contactos: 
    def GET(self):
        return render.lista_contactos()
    
class Ver:
    def GET(self):
        return render.ver()
    

    def POST(self):
        formulario = web.input()
        id = int(formulario ['id'])
        nombre= str(formulario ['nombre'])
        primer_apellido= str(formulario ['primer_apellido'])
        segundo_apellido= str(formulario ['segundo_apellido'])
        telefono= str(formulario ['telefono'])
        email= str(formulario ['email'])

        operacion = formulario.get('operacion')    

class Editar:
    def GET(self):
        return render.editar()    
    
class Borrar:
    def GET(self):
        return render.borrar()  

class Insertar:
    def GET(self):
        return render.insertar()      

if __name__ == "__main__":
    app.run()