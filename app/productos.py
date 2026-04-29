PRODUCTOS = {
    1: {"nombre": "Notebook Lenovo", "precio": 850000, "categoria": "Tecnologia"},
    2: {"nombre": "Mouse Logitech", "precio": 25000, "categoria": "Tecnologia"},
    3: {"nombre": "Teclado Mecanico", "precio": 45000, "categoria": "Tecnologia"},
    4: {"nombre": "Monitor 24 pulgadas", "precio": 320000, "categoria": "Tecnologia"},
    5: {"nombre": "Auriculares Bluetooth", "precio": 18000, "categoria": "Accesorios"},
    6: {"nombre": "Cable HDMI 2m", "precio": 5500, "categoria": "Accesorios"},
    7: {"nombre": "Webcam HD", "precio": 35000, "categoria": "Accesorios"},
    8: {"nombre": "Pendrive 64GB", "precio": 8500, "categoria": "Accesorios"},
}


def obtener_producto(id_producto):
    return PRODUCTOS.get(id_producto)


def listar_productos():
    return PRODUCTOS
