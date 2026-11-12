from typing import TypeVar, Generic
T = TypeVar("T")

MAX_GlOBAL_VALUE = 100 #Max Value a thing in Lager can have

class lager(Generic[T]): #Generic typing lager
    ben = 4 #Klassvariabler (alting har 4 ben)
    def __init__(self, antal, name, typ = T):
        self.antal = antal #Instansvariabel (unika värden pär skapad lager)
        self.typ = typ #Instansvariabel
        self.name = name #Instansvariabel
        Value = 0 #Lokal variabel (finns bara när __init__ körs)

        def show_antal(self):
            return self.antal #LEGB variabel, (nästlad i den här defen ej kall bar utanför)



    #1. skillnad mellan klass och lokal variabel?
    #En klassvariabel skapas när koden börjar köras och är kvar så länge koden körs medan en Lokalvariabel skapas ändast när classen anropas och försvinner där efter

    #2. Varför kan inte den inre (nästlade) funktionen nå variabler som skapats inuti en helt annan metod i samma klass?
    # En nästlad funktion kan inte läsa saker från en annan funktion pga LEGB regeln, då den hoppar mellan (L) Local till (E) Enclosing och sedan till (G) Global vilket gör att den hoppar över att läsa andra funktioner och istället går till Global som är utanför detta
