import unittest
from datetime import date, timedelta
from SRC.services.prestamoService.prestamoBuild import PrestamoBuilder

class TestPrestamoBuilder(unittest.TestCase):

    def test_creacion_basica(self):
        builder = PrestamoBuilder()
        prestamo = (
            builder
            .set_socio("Juan Perez")
            .set_libro("1984 - George Orwell")
            .build()
        )

        #Comprobando que el builder construya correctamente el objeto "Prestamo"

        self.assertEqual(prestamo.socio,"Juan Perez")
        self.assertEqual(prestamo.libro,"1984 - George Orwell")
        self.assertEqual(prestamo.fecha_vencimiento,date.today()+timedelta(days=7))




if __name__ == "__main__":
    unittest.main()        