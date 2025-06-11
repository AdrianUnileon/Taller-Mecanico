from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.MecanicoVO import MecanicoVO
from datetime import date
import jpype
import jpype.imports
from java.sql import Date as JavaSqlDate


class MecanicoDAO(Conexion):

    def _obtener_siguiente_id_mecanico(self) -> int:
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDMecanico) FROM Mecanicos")
            resultado = cursor.fetchone()
            return (resultado[0] or 0) + 1
        except Exception as e:
            print("Error al obtener el siguiente ID del mecánico:", e)
            return 1
        finally:
            if cursor:
                cursor.close()

    def insertar(self, mecanico: MecanicoVO) -> int:
        cursor = None
        try:
            nuevo_id_mecanico = self._obtener_siguiente_id_mecanico()
            cursor = self.getCursor()

            if isinstance(mecanico.FechaContratacion, date):
                java_fecha = JavaSqlDate.valueOf(str(mecanico.FechaContratacion))
            else:
                raise ValueError("FechaContratacion debe ser datetime.date")

            query = """
                INSERT INTO Mecanicos (IDMecanico, IDUsuario, Especialidad, FechaContratacion)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (
                nuevo_id_mecanico,
                mecanico.IDUsuario,
                mecanico.Especialidad,
                java_fecha
            ))

            self.conexion.jconn.commit()
            return nuevo_id_mecanico

        except Exception as e:
            print("Error al insertar mecánico:", e)
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error al hacer rollback: {rollback_error}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_mecanicos_disponibles(self) -> list[dict]:
        try:
            cursor = self.getCursor()
            query = """
                SELECT m.IDMecanico, u.Nombre, u.Apellidos
                FROM Mecanicos m
                JOIN Usuarios u ON m.IDUsuario = u.IDUsuario
                WHERE m.IDMecanico NOT IN (
                    SELECT os.IDMecanico
                    FROM ordenesservicio os
                    WHERE os.Estado = 'Asignada'
                )
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            return [
                {
                    'IDMecanico': row[0],
                    'Nombre': row[1],
                    'Apellidos': row[2]
                } for row in resultados
            ]
        except Exception as e:
            print("Error al obtener mecánicos disponibles:", e)
            return []
        finally:
            if cursor:
                cursor.close()

    def obtener_id_por_usuario(self, id_usuario: int) -> int | None:
        try:
            cursor = self.getCursor()
            query = "SELECT IDMecanico FROM Mecanicos WHERE IDUsuario = ?"
            cursor.execute(query, (id_usuario,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error al obtener ID de mecánico: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def obtener_mecanico_por_usuario(self, id_usuario: int) -> int | None:
        try:
            cursor = self.getCursor()
            query = "SELECT IDMecanico FROM Mecanicos WHERE IDUsuario = ?"
            cursor.execute(query, (id_usuario,))
            row = cursor.fetchone()
            return row[0] if row else None
        except Exception as e:
            print("Error en obtener_mecanico_por_usuario:", e)
            return None
        finally:
            if cursor:
                cursor.close()