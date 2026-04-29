# TPO2: Automatizacion de pruebas y pipeline CI/CD

## Estructura del proyecto

```
TestingAplicaciones-TPO2-Automatizacion_Pruebas_CICD/
├── app/
│   ├── __init__.py
│   ├── descuentos.py        # Logica principal del sistema de descuentos
│   ├── cupones.py           # Gestion de cupones
│   └── productos.py         # Catalogo de productos
├── tests/
│   ├── __init__.py
│   └── test_descuentos.py   # Casos de prueba con pytest
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline CI/CD con GitHub Actions
├── main.py                  # Menu interactivo principal
├── requirements.txt
├── .gitignore
└── README.md
```

## Reglas de negocio

| Regla | Condicion | Descuento |
|-------|-----------|-----------|
| Por monto | Compra > $100,000 | 10% |
| Por cupon | Cupon valido | Variable (segun cupon) |
| Por cantidad | 5+ unidades | 5% |
| Tope maximo | Siempre | 40% maximo |
| Combinacion | Se suman los descuentos aplicables | Hasta el tope |

## Cupones disponibles

| Codigo | Descuento |
|--------|-----------|
| PROMO20 | 20% |
| MEGA50 | 50% |
| DESCUENTO10 | 10% |