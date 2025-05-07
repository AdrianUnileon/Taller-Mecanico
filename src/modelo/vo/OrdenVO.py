class OrdenVO:
    def __init__(self, id_orden=None, fecha=None, descripcion=None, estado=None, id_vehiculo=None, id_mecanico=None):
        self.id_orden = id_orden
        self.fecha = fecha
        self.descripcion = descripcion
        self.estado = estado
        self.id_vehiculo = id_vehiculo
        self.id_mecanico = id_mecanico
