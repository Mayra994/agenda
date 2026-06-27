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


if __name__ == "__main__":
    app.run()