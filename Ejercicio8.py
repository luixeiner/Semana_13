from datetime import date


def diferencias_dias(fecha1, fecha2):
    return (fecha1 - fecha2).days


ahora = date.today()
luis_turin = date(2003, 2, 12)
resultado = diferencias_dias(luis_turin, ahora)
print(resultado)