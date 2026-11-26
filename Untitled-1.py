"""
Problema 3: Reabastecimiento de inventario
Formato de la matriz: [Código, Nombre, Stock actual, Stock mínimo requerido]
"""


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """Devuelve la cantidad exacta a pedir de un artículo.

    Si el stock actual es menor que el mínimo, pide la diferencia;
    en caso contrario (mayor o igual), pide cero.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def mostrar_reporte(inventario):
    """Recorre la matriz y muestra cada artículo con la cantidad a pedir."""
    print("=" * 50)
    print("REPORTE DE REABASTECIMIENTO")
    print("=" * 50)
    print(f"{'Artículo':<25}{'Cantidad a pedir':>20}")
    print("-" * 50)

    total_a_reabastecer = 0
    for fila in inventario:
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]

        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"{nombre:<25}{cantidad:>20}")

        if cantidad > 0:
            total_a_reabastecer += 1

    print("-" * 50)
    print(f"Artículos que requieren reabastecimiento: {total_a_reabastecer}")


def main():
    # Matriz: [Código, Nombre, Stock actual, Stock mínimo requerido]
    inventario = [
        ["A001", "Teclado",        8, 15],
        ["A002", "Mouse",         25, 20],
        ["A003", "Monitor",        3, 10],
        ["A004", "Cable HDMI",    12, 12],
        ["A005", "Memoria USB",    5, 30],
        ["A006", "Disco externo",  9,  6],
    ]

    mostrar_reporte(inventario)


if __name__ == "__main__":
    main()
