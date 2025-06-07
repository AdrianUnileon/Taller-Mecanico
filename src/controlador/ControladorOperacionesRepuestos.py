from src.modelo.UserDao.RepuestoDAO import RepuestoDAO
from src.modelo.vo.RepuestoVO import RepuestoVO

class ControladorOperacionesRepuestos:
    def __init__(self):
        self.dao = RepuestoDAO()

    def insertar_repuesto(self, nombre, cantidad, ubicacion, precio_unitario, id_proveedor):
        repuesto = RepuestoVO(
            Nombre=nombre,
            Cantidad=cantidad,
            Ubicacion=ubicacion,
            PrecioUnitario=precio_unitario,
            IDProveedor=id_proveedor
        )
        return self.dao.insertar(repuesto)  

    def obtener_repuestos(self):
        return self.dao.obtener_todos()  

    def modificar_repuesto(self, id_repuesto, nombre, nueva_cantidad, nueva_ubicacion, nuevo_precio_unitario):
        self.dao.modificar_repuesto(id_repuesto, nombre, nueva_cantidad, nueva_ubicacion, nuevo_precio_unitario)

    def eliminar_repuesto(self, id_repuesto):
        self.dao.eliminar(id_repuesto)
