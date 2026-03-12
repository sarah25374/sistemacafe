from cafe import *

def main():

    # Clientes
    c1 = Cliente(1, "Juan", "juan@email.com")
    c2 = Cliente(2, "Ana", "ana@email.com")

    # Empleados
    c3 = Empleado(3, "Carlos", "carlos@email.com", 101, Rol.BARISTA)
    c4 = Empleado(4, "Laura", "laura@email.com", 102, Rol.MESERO)

    # Bebidas
    c5 = Bebida(1, "Latte", 50, "Grande", "Caliente")
    c6 = Bebida(2, "Cappuccino", 45, "Mediano", "Caliente")

    # Postres
    c7 = Postre(3, "Brownie", 35, False, False)
    c8 = Postre(4, "Galleta Vegana", 30, True, True)

    # Pedido
    c9 = Pedido(1)

    # Inventario
    c10 = Inventario()

    # Login de personas
    c1.login()
    c2.login()
    c3.login()

    # Inventario
    c10.agregarIngrediente("Cafe", 10)
    c10.agregarIngrediente("Leche", 8)
    c10.notificarFaltante("Cafe")

    # Extras a bebidas
    c5.agregarExtra("Leche extra")
    c6.agregarExtra("Chocolate")

    # Agregar productos al pedido
    c9.agregarProducto(c5)
    c9.agregarProducto(c6)
    c9.agregarProducto(c7)
    c9.agregarProducto(c8)

    # Validar stock
    c9.validarStock()

    # Calcular total
    c9.calcularTotal()

    # Cliente realiza pedido
    c1.realizarPedido(c9)

    # Ver historial
    c1.consultarHistorial()

    # Cambiar estado del pedido
    c4.cambiarEstadoPedido(c9, EstadoPedido.PREPARANDO)
    c4.cambiarEstadoPedido(c9, EstadoPedido.ENTREGADO)

    # Canjear puntos
    c1.puntosFidelidad = 120
    c1.canjearPuntos()

    # Actualizar inventario
    c3.actualizarInventario(c10, "Cafe", 2)

if __name__ == "__main__":
    main()