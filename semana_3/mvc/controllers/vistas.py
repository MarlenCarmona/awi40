import web
import time

class Visitas:
    def GET(self, nombre):
      try:
        cookie = web.cookies()
        print(cookie)
        if nombre:
          web.setcookie("nombre",nombre,expires="",domain=None)
        else:
          nombre = "ANONIMO"
          web.setcookie("nombre",nombre,expires="", domain=None)

        if cookie.get("visitas"):
          visitas = int(cookie.get("visitas"))
          visitas += 1
          web.setcookie("visitas", str(visitas), expires="", domain=None)
        else:
          web.setcookie("visitas", str(1), expires="", domain=None)

        return " Visitas " + str(visitas ) + " Nombre " + nombre + "Hora: " + time.strftime("%H:%M:%S") + " Fecha: " + time.strftime("%d:%m:%Y")
      except Exception as e:  
        return "Error"+str(e.args)