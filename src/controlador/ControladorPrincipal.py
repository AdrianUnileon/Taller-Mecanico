class ControladorPrincipal():
    def __init__(self, vista, modelo):
        self._vista = vista
        self._modelo = modelo
    
    def login(self, nombre):
        if len (nombre) >3:
            loginVO = loginVO(nombre)
            respuestaLogin = self._modelo.comprobarLogin(loginVO)
            print(respuestaLogin)
        else:
            print("Nombre invalido")

    def mostrarLogin(self):
        self._vista.show()

    def ocultarLogin(self):
        self._vista.hide()
