from app.cupones import validar_cupon

MONTO_MINIMO_DESCUENTO = 100000
DESCUENTO_POR_MONTO = 10
CANTIDAD_MINIMA_DESCUENTO = 5
DESCUENTO_POR_CANTIDAD = 5
TOPE_MAXIMO_DESCUENTO = 40


class CalculadoraDescuentos:

    def calcular_descuento(self, monto, cupon=None, cantidad=1):
        self._validar_entradas(monto, cantidad)

        descuento_total = 0

        # chequeo si aplica descuento por monto
        if monto > MONTO_MINIMO_DESCUENTO:
            descuento_total += DESCUENTO_POR_MONTO

        info_cupon = validar_cupon(cupon)
        if info_cupon:
            descuento_total += info_cupon["descuento"]

        if cantidad >= CANTIDAD_MINIMA_DESCUENTO:
            descuento_total += DESCUENTO_POR_CANTIDAD

        # me aseguro de no pasar el tope
        if descuento_total > TOPE_MAXIMO_DESCUENTO:
            descuento_total = TOPE_MAXIMO_DESCUENTO

        descuento_monto = round(monto * descuento_total / 100, 2)
        monto_final = round(monto - descuento_monto, 2)

        return {
            "monto_original": monto,
            "descuento_porcentaje": descuento_total,
            "descuento_monto": descuento_monto,
            "monto_final": monto_final
        }

    def _validar_entradas(self, monto, cantidad):
        if not isinstance(monto, (int, float)):
            raise ValueError("El monto debe ser un numero")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0")
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un numero entero")
        if cantidad < 1:
            raise ValueError("La cantidad debe ser mayor o igual a 1")
