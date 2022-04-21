class Proyecto:


    def _init_(self, apps, tiempo,consejos):
        
        self.apps = apps
        self.tiempo = tiempo
        self.conejos = consejos
        pass
    class configuracion:
        def _init_(self, ocupacion, edad,horas_invertida,color,estado_civil,peso) -> None:
            self.ocupacion = ocupacion
            self.edad = edad
            self.horas_invertida = horas_invertida
            self.color = color 
            self.estado_civil = estado_civil
            self.peso = peso
            pass
    class aplicacion:

        def _init_(self, color,tipo,consejo):

            self.color = color
            self.tipo = tipo
            self.consejo = consejo    
            pass
    class facebook:
        def _init_(self) -> None:
            pass
    class instagram:
        def _init_(self) -> None:
            
    class wpp:
        def _init_(self) -> None:
            pass
    
    menu = ("
    1facebook
    2instagram
    3wpp
    4salir ")
    eleccion = int(input("elige"))
    switch eleccion :
        case 1:
            print("facebook")
            break
        case 2:
            print("instragram")
            break
        case 3:
            print("wpp")
            break

        
    class aplicaconjuego:

    def _init_(self, tipo, consej) :

        self.tipo = tipo
        self.consej = consej
        pass
    class leagueoflegends:
        def _init_(self) -> None:
            
    class friv:
        def _init_(self) -> None:
            pass
    class yandere_simulator:
        def _init_(self) -> None:
            pass
    
    juego = ("bienvenido.
    1leagueoflegends
    2friv
    3yandere_simulator
    4salir ")
    opcion = int(input("elige"))
    switch eleccion :
        case 1:
            print("leagueoflegends")
            break
        case 2:
            print("friv")
            break
        case 3:
            print("yandere_simulator")
            break
        
    class tiempo: 
    
    def _init_(self,hora,limite) -> None:
        self.limite = horau
        self.hora
        pass

        def tiempo(self):
            
            while hora == limite:
                print("ya haz pasado tu limite. Sal a la calle, juega algo.")
