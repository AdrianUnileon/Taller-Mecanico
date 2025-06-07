class ControladorAdministrador:
    def __init__(self):
        self.view = None

    def iniciar(self):
        from src.vista.AdministradorPanel import AdministradorPanel 
        self.view = AdministradorPanel(self)
        self.view.show()
