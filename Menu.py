import xml.etree.ElementTree as ET

class Nodo:
    def __init__(self, dato) -> None:
        self.dato = None
        self.siguiente = None
        self.matriz

class Nodo2:
    def __init__(self,nombre,id,matriz) -> None:
        self.nombre = nombre
        self.id = id
        self.matriz = matriz

class Lista:
    def __init__(self) -> None:
        self.cabeza = None
        self.q = None
        
    def insertar(self, nodo):
        p = nodo
        p.siguiente = None
        if self.cabeza == None:
            self.cabeza = p
        else:
            self.q.siguiente = p
        self.q = p
    
    def pop(self):
        temp = ""
        if self.cabeza is not None:
            temp = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
        return temp

class Menu:

    def __init__(self) -> None:
        pass

    def menu(self):
        print("1.Leer Archivo")
        print("2.Buscar y Mostrar")
        print("3.Eliminar Fila")
        print("4.Comparar")
        print("5.Buscar")
        print("6.Salir")
        op = input("Seleccione la opcion ")
        if(op is "1"):
            archivo = input("Ingrese el archivo: ")
            tree = ET.parse(archivo)
            root = tree.getroot()
            for elemento in root:
                n = elemento.get('n')
                m = elemento.get('m')
                nombre = elemento.get('nombre')
                datos = Lista()
                for subelemento in elemento:
                    dato = subelemento.text
                    datos.insertar(Nodo(dato))
        
        elif(op is "2"):
            pass
        elif(op is "3"):
            pass
        elif(op is "4"):
            pass
        elif(op is "5"):
            pass
        elif(op is "6"):
            pass
                






