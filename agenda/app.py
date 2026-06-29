import web  
urls = (
    '/', 'controllers.index.Index',
    '/contactos', 'controllers.lista_contactos.Contactos',
    '/ver', 'controllers.ver.Ver',
    '/editar','controllers.editar.Editar',
    '/borrar','controllers.borrar.Borrar',
    '/insertar','controllers.insertarInsertar'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()