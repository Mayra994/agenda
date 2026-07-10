import web  
urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos','controllers.lista_contactos.ListaContactos',
    '/ver_contacto/(.*)','controllers.ver_contacto.VerContacto',
    '/editar_contacto/(.*)','controllers.editar_contacto.EditarContacto',
    '/borrar/(.*)','controllers.borrar.BorrarContacto',
    '/insertar','controllers.insertar.InsertarContacto'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()