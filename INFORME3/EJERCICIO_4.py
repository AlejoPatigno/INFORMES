import json
archivo= "empleados.json"
ruta = "INFORME3/" + archivo
opcion = "r"
with open(ruta, opcion) as file:
    data = json.load(file)

print("lectura de datos=>", data)



class Empresa:
    #Para crear los atributos
    def __init__(self, nombre: str, ciudad: str, empleados: list):
        self.nombre = nombre
        self.ciudad = ciudad
        self.empleados = empleados
    
    #Para crear metodos (funciones)
    def cargarEmpleados(self, archivo: str):
        import json
        ruta = archivo
        opcion = "r"
        with open(ruta, opcion) as file:
            data = json.load(file)
        print("lectura de datos=>", data)
        return data

    def leerEmpleados(self):
        empleados= data
        listaEmpleados = []
        for i in range(0,len(empleados)):
            listaEmpleados.append(empleados[i]["nombre"])
        return listaEmpleados   
    
    def agregarNuevoEmpleado(self, nombre: str, codigo: str, edad: int , cargo: str , añosExperiencia: int):
        empleados= data
        nuevoEmpleado = {"nombre": nombre , "codigo": codigo, "edad": edad, "cargo": cargo, "añosExperiencia":añosExperiencia}
        empleados.append(nuevoEmpleado)

    def eliminarEmpleado(self, codigo: str):
        empleados= data
        lista=[]
        for i in empleados:
            lista.append(i["codigo"])
        if codigo in lista:
            posicion=lista.index(codigo)
            empleados.pop(posicion)

    


#Como creo el objeto ?
empresa1 = Empresa("software Colombia", "manizales",[])

empresa1.cargarEmpleados("INFORME3/empleados.json")
empresa1.agregarNuevoEmpleado("Juan Posada", "100", 30, "Jefe", 1)
empresa1.eliminarEmpleado("001")
empresa1.eliminarEmpleado("002")
empresa1.eliminarEmpleado("003")
empresa1.cargarEmpleados("INFORME3/empleados.json")

listaEmpleados = empresa1.leerEmpleados()