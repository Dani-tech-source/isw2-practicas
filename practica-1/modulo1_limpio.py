"""Versión refactorizada de modulo1_antes.py aplicando Clean Code.

Hace exactamente lo mismo que el código original en los pedidos válidos:
verifica existencias, calcula el total con descuento e ISV, descuenta el
inventario y avisa al cliente.
"""
from dataclasses import dataclass

TASA_ISV = 0.15

PORCENTAJE_DESCUENTO = {
    "ninguno": 0.00,
    "cliente_frecuente": 0.10,
    "mayorista": 0.20,
}


class StockInsuficiente(Exception):
    pass


@dataclass
class Repuesto:
    nombre: str
    precio: float
    existencias: int


def realizar_pedido(inventario, cliente, lineas, tipo_descuento="ninguno"):
    verificar_existencias(inventario, lineas)
    total = calcular_total(inventario, lineas, tipo_descuento)
    descontar_existencias(inventario, lineas)
    notificar_cliente(cliente, total)
    return total


def verificar_existencias(inventario, lineas):
    for codigo, cantidad in lineas:
        repuesto = inventario[codigo]
        if repuesto.existencias < cantidad:
            raise StockInsuficiente(
                f"Solo quedan {repuesto.existencias} unidades de {repuesto.nombre}"
            )


def calcular_total(inventario, lineas, tipo_descuento):
    subtotal = calcular_subtotal(inventario, lineas)
    subtotal_con_descuento = aplicar_descuento(subtotal, tipo_descuento)
    return subtotal_con_descuento * (1 + TASA_ISV)


def calcular_subtotal(inventario, lineas):
    return sum(inventario[codigo].precio * cantidad for codigo, cantidad in lineas)


def aplicar_descuento(subtotal, tipo_descuento):
    if tipo_descuento not in PORCENTAJE_DESCUENTO:
        raise ValueError(f"Tipo de descuento desconocido: {tipo_descuento}")
    return subtotal * (1 - PORCENTAJE_DESCUENTO[tipo_descuento])


def descontar_existencias(inventario, lineas):
    for codigo, cantidad in lineas:
        inventario[codigo].existencias -= cantidad


def notificar_cliente(cliente, total):
    print(f"Correo a {cliente}: su total es L {total:.2f}")


if __name__ == "__main__":
    inventario = {
        "FIL-001": Repuesto("Filtro de aceite", 450, 10),
        "PAS-002": Repuesto("Pastillas de freno", 1500, 4),
    }
    realizar_pedido(
        inventario,
        "dani@correo.com",
        [("FIL-001", 2), ("PAS-002", 1)],
        "cliente_frecuente",
    )