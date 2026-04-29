from app.descuentos import CalculadoraDescuentos
from app.productos import listar_productos, obtener_producto
from app.cupones import CUPONES, validar_cupon


def mostrar_menu():
    print("\n" + "=" * 50)
    print("       SISTEMA DE DESCUENTOS - E-COMMERCE")
    print("=" * 50)
    print("1. Ver catalogo de productos")
    print("2. Comprar un producto")
    print("3. Ver cupones disponibles")
    print("4. Salir")
    print("-" * 50)


def mostrar_catalogo():
    productos = listar_productos()
    print("\n" + "-" * 50)
    print("           CATALOGO DE PRODUCTOS")
    print("-" * 50)
    print(f"{'ID':<4} {'Producto':<25} {'Precio':>10} {'Categoria'}")
    print("-" * 50)
    for id_prod, prod in productos.items():
        print(f"{id_prod:<4} {prod['nombre']:<25} ${prod['precio']:>9,.2f} {prod['categoria']}")
    print("-" * 50)


def mostrar_cupones():
    print("\n" + "-" * 50)
    print("           CUPONES DISPONIBLES")
    print("-" * 50)
    print(f"{'Codigo':<15} {'Descuento':>10}  {'Descripcion'}")
    print("-" * 50)
    for codigo, info in CUPONES.items():
        print(f"{codigo:<15} {info['descuento']:>9}%  {info['descripcion']}")
    print("-" * 50)


def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"  El valor debe ser al menos {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  El valor debe ser como maximo {maximo}.")
                continue
            return valor
        except ValueError:
            print("  Ingrese un numero valido.")


def flujo_compra():
    calc = CalculadoraDescuentos()

    mostrar_catalogo()

    id_prod = leer_entero("\nIngrese el ID del producto: ", minimo=1)
    producto = obtener_producto(id_prod)

    if not producto:
        print("  Producto no encontrado. Intente de nuevo.")
        return

    print(f"\n  Producto seleccionado: {producto['nombre']} - ${producto['precio']:,.2f}")

    cantidad = leer_entero("  Ingrese la cantidad: ", minimo=1)

    monto_total = producto["precio"] * cantidad
    print(f"  Subtotal ({cantidad} x ${producto['precio']:,.2f}): ${monto_total:,.2f}")

    cupon = input("\n  Ingrese un cupon de descuento (o ENTER para continuar sin cupon): ").strip()
    if not cupon:
        cupon = None
    else:
        if not validar_cupon(cupon):
            print(f"  El cupon '{cupon.upper()}' no es valido. Se continuara sin descuento por cupon.")
            cupon = None

    try:
        resultado = calc.calcular_descuento(
            monto=monto_total, cupon=cupon, cantidad=cantidad
        )
    except ValueError as e:
        print(f"\n  Error: {e}")
        return

    print("\n" + "=" * 50)
    print("             RESUMEN DE COMPRA")
    print("=" * 50)
    print(f"  Producto:        {producto['nombre']}")
    print(f"  Precio unitario: ${producto['precio']:,.2f}")
    print(f"  Cantidad:        {cantidad}")
    print(f"  Subtotal:        ${resultado['monto_original']:,.2f}")

    if resultado["descuento_porcentaje"] > 0:
        print(f"  Descuento:       {resultado['descuento_porcentaje']}% (-${resultado['descuento_monto']:,.2f})")
    else:
        print("  Descuento:       Sin descuento")

    if cupon:
        print(f"  Cupon aplicado:  {cupon.upper()}")

    print("-" * 50)
    print(f"  TOTAL A PAGAR:   ${resultado['monto_final']:,.2f}")
    print("=" * 50)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            flujo_compra()
        elif opcion == "3":
            mostrar_cupones()
        elif opcion == "4":
            print("\nGracias por su visita!")
            break
        else:
            print("\n  Opcion invalida. Intente de nuevo.")


if __name__ == "__main__":
    main()
