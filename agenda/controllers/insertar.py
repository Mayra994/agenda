import web
import sqlite3

render = web.template.render("views", base="layout")


class BorrarContacto:

    def eliminarContacto(self, id_contacto: int) -> bool:
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect("sql/agenda.db")
            cursor = conn.cursor()
            # Consulta para eliminar el registro de la tabla contactos
            query = "DELETE FROM contactos WHERE id_contacto = ?;"
            cursor.execute(query, (id_contacto,))
            conn.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR borrarContacto 102: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR borrarContacto 103: {error.args}")
            return False
        finally:
            conn.close()

    def obtenerContacto(self, id_contacto=None):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect("sql/agenda.db")
            cursor = conn.cursor()
            # Consulta los datos del registro a confirmar
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            row = cursor.fetchone()
            
            if row is None:
                return {}

            contacto = {
                "id_contacto": row[0],
                "nombre": row[1],
                "primer_apellido": row[2],
                "segundo_apellido": row[3],
                "email": row[4],
                "telefono": row[5],
            }
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR borrarContacto 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR borrarContacto 101: {error.args}")
            return {}
        finally:
            conn.close()

    def GET(self, id_contacto=None):
        print(f"ID_CONTACTO A BORRAR (GET): {id_contacto}")
        contacto = self.obtenerContacto(id_contacto)
        print(contacto)
        
        # Muestra la plantilla de confirmación pasando los datos actuales
        return render.insertar(contacto)  # type: ignore

    def POST(self, id_contacto=None):
        print(f"ID_CONTACTO A BORRAR (POST): {id_contacto}")
        formulario = web.input()
        
        # Obtenemos el id del formulario o de la URL
        id_borrar = formulario.get("id_contacto", id_contacto)
        
        # Se ejecuta la lógica de borrado estructurada arriba
        resultado = self.eliminarContacto(id_borrar)
        
        if resultado:
            # Si se borró con éxito, redirige de vuelta a la lista
            raise web.seeother('/lista_contactos')
        else:
            return "Error al intentar borrar el contacto."