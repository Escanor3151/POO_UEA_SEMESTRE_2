class CallCenter:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area


    def imprimir_cliente(self):
        return f"El cliente {self.nombre}, pertenece al area de: {self.area}"

class Requerimiento(CallCenter):
    def __init__(self, nombre, area, metodo_comunicacion, nro_requerimiento):
        super().__init__(nombre, area )
        self.metodo_comunicacion = metodo_comunicacion
        self.nro_requerimiento = nro_requerimiento

    def imprimir_metodo(self):
        return f"El cliente {self.nombre}, pertenece al area de: {self.area} se comunico por: {self.metodo_comunicacion}"

    def agregar_requerimiento(self, requerimiento, nro_requerimiento):
        self.requerimiento = requerimiento
        self.__nro_requerimiento = nro_requerimiento
        if requerimiento == 'Soporte':
            self.__nro_requerimiento += 1
            print(f"Se agrego un nuevo requerimiento de Soporte. Numero de requerimientos atentido: {self.__nro_requerimiento}")
            return "El requerimiento es Soporte"
        elif requerimiento == 'Visita':
            self.__nro_requerimiento += 1
            print(f"Se agrego un nuevo requerimiento de Visita. Numero de requerimientos atentido: {self.__nro_requerimiento}")
            return "El requerimiento es Visita"
        else:
            return "El requerimiento no es valido"

    def imprimir_requerimiento(self):
        return self.__nro_requerimiento

mis_datos = CallCenter("Charlie Cuaces", "Hogar")
print(mis_datos.imprimir_cliente())
mi_requerimeinto = Requerimiento("Charlie Cuaces", "Hogar", "Chat", 3)
print(mi_requerimeinto.imprimir_metodo())
mi_requerimeinto.agregar_requerimiento("Soporte", 3)

