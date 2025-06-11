from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.RecepcionistaVO import RecepcionistaVO

class RecepcionistaDAO(Conexion):

    def _obtener_siguiente_id_recepcionista(self) -> int:
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDRecepcionista) FROM Recepcionistas")
            resultado = cursor.fetchone()
            return (resultado[0] or 0) + 1
        except Exception as e:
            print("Error al obtener el siguiente ID del recepcionista:", e)
            return 1
        finally:
            if cursor:
                cursor.close()

    def insertar(self, recepcionista: RecepcionistaVO) -> int:
        try:
            nuevo_id_recepcionista = self._obtener_siguiente_id_recepcionista()
            cursor = self.getCursor()
            query = """
                INSERT INTO Recepcionistas (IDRecepcionista, IDUsuario, Turno)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (
                nuevo_id_recepcionista,
                recepcionista.IDUsuario,
                recepcionista.Turno,
            ))
            self.conexion.jconn.commit()
            return nuevo_id_recepcionista
        except Exception as e:
            print("Error al insertar recepcionista:", e)
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error al hacer rollback: {rollback_error}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_id_por_usuario(self, id_usuario: int) -> int | None:
        try:
            cursor = self.getCursor()
            query = "SELECT IDRecepcionista FROM Recepcionistas WHERE IDUsuario = ?"
            cursor.execute(query, (id_usuario,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except Exception as e:
            print("Error en obtener_id_por_usuario:", e)
            return None
        finally:
            if cursor:
                cursor.close()


