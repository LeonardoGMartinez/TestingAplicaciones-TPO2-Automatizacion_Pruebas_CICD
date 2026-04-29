CUPONES = {
    "PROMO20": {"descuento": 20, "descripcion": "20% de descuento promocional"},
    "MEGA50": {"descuento": 50, "descripcion": "50% de descuento mega oferta"},
    "DESCUENTO10": {"descuento": 10, "descripcion": "10% de descuento basico"},
}


def validar_cupon(codigo):
    if not codigo or not isinstance(codigo, str):
        return None
    return CUPONES.get(codigo.upper())
