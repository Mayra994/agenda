import web

render = web.template.render('views/')

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
