from src.modelo.Servicios.ServicioFactura import ServicioFactura

class ControladorFacturas:
    def __init__(self):
        self.servicio = ServicioFactura()

    def obtener_ordenes_para_factura(self) -> list:
        """
        Obtiene las órdenes disponibles para facturar
        :return: Lista de órdenes finalizadas sin factura
        """
        return self.servicio.obtener_ordenes_para_factura()

    def generar_factura(self, id_orden: int, precio_sin_iva_y_beneficio: float, id_recepcionista: int) -> bool:
        """
        Genera una nueva factura
        :param id_orden: ID de la orden a facturar
        :param precio_sin_iva_y_beneficio: Precio total de la factura
        :param id_recepcionista: ID del recepcionista que genera la factura
        :return: True si la operación fue exitosa, False en caso contrario
        """
        return self.servicio.generar_factura(id_orden, precio_sin_iva_y_beneficio, id_recepcionista)

