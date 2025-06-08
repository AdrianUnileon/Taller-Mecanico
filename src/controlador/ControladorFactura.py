from src.modelo.UserDao.FacturaDAO import FacturaDAO

class ControladorFacturas:
    def __init__(self):
        self.factura_dao = FacturaDAO()

    def obtener_ordenes_para_factura(self):
        return self.factura_dao.obtener_ordenes_finalizadas()

    def generar_factura(self, id_orden, precio_sin_iva_y_beneficio, id_recepcionista):
        return self.factura_dao.generar_factura_por_orden(id_orden, precio_sin_iva_y_beneficio, id_recepcionista)

