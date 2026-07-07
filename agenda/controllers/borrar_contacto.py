import web
import sqlite3

render = web.template.render('views/', base='layout')

class BorrarContacto:

    def borrarContacto(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            row = cursor.fetchone()
            contacto = {
                'id_contacto': row[0],
                'nombre': row[1]
            }
            conn.close()
            return contacto
        except Exception as error:
            print(f"Error: {error}")
            return {}

    def GET(self, id_contacto):
        contacto = self.borrarContacto(id_contacto)
        return render.borrar_contacto(contacto)

    def POST(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (int(id_contacto),))
            conn.commit()
            conn.close()
            raise web.seeother('/lista_contactos')
        except Exception as error:
            print(f"Error: {error}")
            return "No se pudo eliminar el contacto."