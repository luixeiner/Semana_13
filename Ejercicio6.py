import datetime
from time import perf_counter

def mostrarFecha():
    fecha = datetime.datetime.now()
    print(fecha.strftime("%H:%M:%S"))
    print(fecha.utcnow("%H:%M:%S"))
    print(fecha.strftime("%Y-%m-%d"))


mostrarFecha()

