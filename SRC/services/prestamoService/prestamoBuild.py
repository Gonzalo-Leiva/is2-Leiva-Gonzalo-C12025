from datetime import date, timedelta

class Prestamo:
    def __init__(self,socio,libro,fecha_inicio,fecha_vencimiento,multa=0):
        self.socio = socio
        self.libro = libro
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.multa = multa

    def __str__(self):
        return f"Préstamo de '{self.libro}' a {self.socio} (multa: ${self.multa})"



class PrestamoBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.socio = None
        self.libro = None
        self.fecha_inicio = date.today()
        self.dias_prestamo = 7
        self.multa = 0
        return self
    
    def set_socio(self, socio):
        self.socio = socio
        return self

    def set_libro(self, libro):
        self.libro = libro
        return self

    def set_dias_prestamo(self, dias):
        self.dias_prestamo = dias
        return self

    def set_multa(self, multa):
        self.multa = multa
        return self

    def build(self):
        vencimiento = self.fecha_inicio + timedelta(days=self.dias_prestamo)
        prestamo = Prestamo(
            socio=self.socio,
            libro=self.libro,
            fecha_inicio=date.today(),
            fecha_vencimiento=vencimiento,
            multa=self.multa
        )
        self.reset()
        return prestamo
