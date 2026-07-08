import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

    def eliminarContactos(self, id_contacto):
        conn = None 
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            # Consulta filtrando específicamente por el ID del contacto
            query = "SELECT * FROM contactos WHERE id_contacto = ?;"
            cursor.execute(query, (id_contacto,))
            
            contactos = []
            # Almacena el registro encontrado en un diccionario
            for row in cursor.fetchall():
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                contactos.append(contacto)

            return contactos
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return []
        finally:
            if conn:
                conn.close()


    def GET(self, id_contacto):
        
        contacto = self.eliminarContactos(id_contacto)
        
     
        if contacto:
            contacto = contacto[0]
       
       

        print(contacto)
        
        
        return render.borrar_contacto(contacto)