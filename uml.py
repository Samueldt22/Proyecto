@startuml
class proyecto {
-Aplicaciones : apps
+consejos : str
+tiempo: str
}

class Aplicacion {
-color: str
-tipo : str
+concejo: str

+tiempo()
}

class wpp {


}

class Instagram {


}

class facebook{

}

class aplicacionjuego{
-tipo : str
+concejo: str
+tiempo()
}

class Leagueoflegends{

}

class yandere_simulator{

}

class friv {
}


class concejos{
+tiempo()
}


proyecto o--  Aplicacion
proyecto o--  aplicacionjuego
aplicacionjuego *-- concejos
Aplicacion *-- concejos
Aplicacion -- wpp
Aplicacion -- Instagram
Aplicacion -- facebook
Aplicacion - aplicacionjuego
aplicacionjuego -- Leagueoflegends
aplicacionjuego -- yandere_simulator
aplicacionjuego -- friv
@enduml
