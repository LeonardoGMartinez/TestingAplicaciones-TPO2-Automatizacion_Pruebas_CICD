import pytest
from app.descuentos import CalculadoraDescuentos


@pytest.fixture
def calculadora():
    return CalculadoraDescuentos()






class TestCasosExitosos:

    def test_descuento_combinado(self, calculadora):
        resultado = calculadora.calcular_descuento(monto=200000, cupon="PROMO20", cantidad=5)
        assert resultado["descuento_porcentaje"] == 35
        assert resultado["monto_final"] == 130000

    def test_con_cupon(self, calculadora):
        resultado = calculadora.calcular_descuento(monto=50000, cupon="PROMO20")
        assert resultado["descuento_porcentaje"] == 20
        assert resultado["monto_final"] == 40000


class TestCasosError:

    def test_monto_negativo(self, calculadora):
        with pytest.raises(ValueError):
            calculadora.calcular_descuento(monto=-500)

    def test_cantidad_con_decimales(self, calculadora):
        with pytest.raises(ValueError):
            calculadora.calcular_descuento(monto=50000, cantidad=2.5)


class TestCasosLimite:


    def test_tope_maximo_40(self, calculadora):
        resultado = calculadora.calcular_descuento(monto=200000, cupon="MEGA50", cantidad=5)
        assert resultado["descuento_porcentaje"] == 40
        assert resultado["monto_final"] == 120000


    def test_monto_justo_en_100000(self, calculadora):
        resultado = calculadora.calcular_descuento(monto=100000)
        assert resultado["descuento_porcentaje"] == 0
        assert resultado["monto_final"] == 100000
