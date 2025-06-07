from src.modelo.UserDao.FacturaDAO import FacturaDAO
from src.modelo.vo.FacturaVO import FacturaVO
from datetime import date

class ControladorFacturas:
    def __init__(self):
        self.factura_dao = FacturaDAO()

    def obtener_ordenes_para_factura(self):
        return self.factura_dao.obtener_ordenes_finalizadas()

    def generar_factura(self, id_orden, costo_mano_obra, id_recepcionista):
        iva = 0.21
        beneficio = 0.15
        total = costo_mano_obra * (1 + iva + beneficio)
        factura = FacturaVO(
            Fecha=date.today(),
            Total=round(total, 2),
            IDOrden=id_orden,
            IDRecepcionista=id_recepcionista
        )
        return self.factura_dao.insertar_factura(factura)

