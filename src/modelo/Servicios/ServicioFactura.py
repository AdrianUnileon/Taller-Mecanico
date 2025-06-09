from src.modelo.UserDao.FacturaDAO import FacturaDAO
from src.modelo.vo.FacturaVO import FacturaVO


class ServicioFactura:
    def __init__(self):
        self.factura_dao = FacturaDAO()

    def obtener_ordenes_para_factura(self) -> list:
        return self.factura_dao.obtener_ordenes_finalizadas()

    def generar_factura(self, id_orden: int, precio_sin_iva_y_beneficio: float, id_recepcionista: int) -> bool:
        return self.factura_dao.generar_factura_por_orden(id_orden, precio_sin_iva_y_beneficio, id_recepcionista)

    def insertar_factura(self, factura: FacturaVO) -> int:
        return self.factura_dao.insertar_factura(factura)

    def obtener_factura_por_id(self, id_factura: int) -> FacturaVO:
        return self.factura_dao.buscar_por_id(id_factura)