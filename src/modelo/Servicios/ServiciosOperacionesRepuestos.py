from src.modelo.UserDao.RepuestoDAO import RepuestoDAO
from src.modelo.vo.RepuestoVO import RepuestoVO

class ServicioOperacionesRepuestos:
    def __init__(self):
        self.dao = RepuestoDAO()

    def obtener_repuestos(self) -> list:
        try:
            return self.dao.obtener_todos()
        except Exception as e:
            print(f"Error al obtener repuestos: {e}")
            return []

    def insertar_repuesto(self, nombre: str, cantidad: int, ubicacion: str, precio_unitario: float, id_proveedor: int) -> bool:
        try:
            if not nombre or cantidad < 0 or precio_unitario <= 0:
                raise ValueError("Datos inválidos para el repuesto")

            repuesto = RepuestoVO(
                Nombre=nombre,
                Cantidad=cantidad,
                Ubicacion=ubicacion,
                PrecioUnitario=precio_unitario,
                IDProveedor=id_proveedor
            )
            return self.dao.insertar(repuesto) > 0
        except Exception as e:
            print(f"Error al insertar repuesto: {e}")
            return False

    def modificar_repuesto(self, id_repuesto: int, nombre: str, cantidad: int, ubicacion: str, precio_unitario: float) -> bool:
        try:
            if not id_repuesto or cantidad < 0 or precio_unitario <= 0:
                raise ValueError("Datos inválidos para modificar el repuesto")

            return self.dao.modificar_repuesto(id_repuesto, nombre, cantidad, ubicacion, precio_unitario)
        except Exception as e:
            print(f"Error al modificar repuesto: {e}")
            return False

    def eliminar_repuesto(self, id_repuesto: int) -> bool:
        try:
            if not id_repuesto or id_repuesto <= 0:
                raise ValueError("ID inválido")

            self.dao.eliminar(id_repuesto)
            return True
        except Exception as e:
            print(f"Error al eliminar repuesto: {e}")
            return False
