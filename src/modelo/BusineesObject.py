from src.modelo.UserDao.userDao import UserDao
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.vo.UserVO import UserVO

class BussinessObject():

    def comprobarLogin(self, loginVO):
        logindao = UserDaoJDBC()
        return logindao.consultaLogin(loginVO)

    def pruebainsert(self):
        user_dao = UserDaoJDBC()
        usuario1 = UserVO(4, "nom", "api", "ap2", "l@gmail.com")
        filas = user_dao.insert(usuario1)
    
    def pruebaselect(self):
        user_dao = UserDaoJDBC()
        usuarios = user_dao.select()
        for usuario in usuarios:
            print(usuario)
            print(usuario.nombre)
        
