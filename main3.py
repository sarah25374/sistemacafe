from cafe import *

# -------- CLIENTES --------
print("\nCLIENTES")

cliente1 = Cliente(1,"Ana","ana@gmail.com")
cliente2 = Cliente(2,"Luis","luis@gmail.com")
cliente3 = Cliente(3,"Maria","maria@gmail.com")
cliente4 = Cliente(4,"Carlos","carlos@gmail.com")
cliente5 = Cliente(5,"Elena","elena@gmail.com")
cliente6 = Cliente(6,"Pedro","pedro@gmail.com")
cliente7 = Cliente(7,"Laura","laura@gmail.com")
cliente8 = Cliente(8,"Sofia","sofia@gmail.com")
cliente9 = Cliente(9,"Diego","diego@gmail.com")
cliente10 = Cliente(10,"Valeria","valeria@gmail.com")

clientes = [cliente1,cliente2,cliente3,cliente4,cliente5,cliente6,cliente7,cliente8,cliente9,cliente10]

for c in clientes:
    print("ID:",c.idPersona,"Nombre:",c.nombre,"Email:",c.email)


# -------- EMPLEADOS --------
print("\nEMPLEADOS")

empleado1 = Empleado(11,"Miguel","miguel@gmail.com",101,Rol.BARISTA)
empleado2 = Empleado(12,"Lucia","lucia@gmail.com",102,Rol.MESERO)
empleado3 = Empleado(13,"Raul","raul@gmail.com",103,Rol.GERENTE)
empleado4 = Empleado(14,"Diana","diana@gmail.com",104,Rol.BARISTA)
empleado5 = Empleado(15,"Jorge","jorge@gmail.com",105,Rol.MESERO)
empleado6 = Empleado(16,"Andrea","andrea@gmail.com",106,Rol.BARISTA)
empleado7 = Empleado(17,"Roberto","roberto@gmail.com",107,Rol.MESERO)
empleado8 = Empleado(18,"Paola","paola@gmail.com",108,Rol.GERENTE)
empleado9 = Empleado(19,"Fernando","fernando@gmail.com",109,Rol.BARISTA)
empleado10 = Empleado(20,"Camila","camila@gmail.com",110,Rol.MESERO)

empleados = [empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9,empleado10]

for e in empleados:
    print("ID:",e.idPersona,"Nombre:",e.nombre,"Rol:",e.rol.value)


# -------- BEBIDAS --------
print("\nBEBIDAS")

bebida1 = Bebida(1,"Latte",50,"Grande","Caliente")
bebida2 = Bebida(2,"Capuccino",55,"Mediano","Caliente")
bebida3 = Bebida(3,"Americano",40,"Grande","Caliente")
bebida4 = Bebida(4,"Mocha",60,"Grande","Caliente")
bebida5 = Bebida(5,"Chocolate",45,"Mediano","Caliente")
bebida6 = Bebida(6,"Frappe",65,"Grande","Frio")
bebida7 = Bebida(7,"Te Chai",50,"Mediano","Caliente")
bebida8 = Bebida(8,"Matcha",55,"Grande","Caliente")
bebida9 = Bebida(9,"Cold Brew",60,"Grande","Frio")
bebida10 = Bebida(10,"Latte Vainilla",70,"Grande","Caliente")

bebidas = [bebida1,bebida2,bebida3,bebida4,bebida5,bebida6,bebida7,bebida8,bebida9,bebida10]

for b in bebidas:
    print("ID:",b.idProducto,"Nombre:",b.nombre,"Precio:",b.precioBase)


# -------- POSTRES --------
print("\nPOSTRES")

postre1 = Postre(1,"Brownie",40,False,False)
postre2 = Postre(2,"Cheesecake",50,False,False)
postre3 = Postre(3,"Galleta",25,False,False)
postre4 = Postre(4,"Pastel Chocolate",60,False,False)
postre5 = Postre(5,"Panque",35,False,False)
postre6 = Postre(6,"Cupcake",30,False,False)
postre7 = Postre(7,"Donut",28,False,False)
postre8 = Postre(8,"Tarta Manzana",45,False,False)
postre9 = Postre(9,"Brownie Vegano",50,True,True)
postre10 = Postre(10,"Pastel Sin Gluten",55,False,True)

postres = [postre1,postre2,postre3,postre4,postre5,postre6,postre7,postre8,postre9,postre10]

for p in postres:
    print("ID:",p.idProducto,"Nombre:",p.nombre,"Precio:",p.precioBase)


# -------- PEDIDOS --------
print("\nPEDIDOS")

pedido1 = Pedido(1)
pedido2 = Pedido(2)
pedido3 = Pedido(3)
pedido4 = Pedido(4)
pedido5 = Pedido(5)
pedido6 = Pedido(6)
pedido7 = Pedido(7)
pedido8 = Pedido(8)
pedido9 = Pedido(9)
pedido10 = Pedido(10)

pedidos = [pedido1,pedido2,pedido3,pedido4,pedido5,pedido6,pedido7,pedido8,pedido9,pedido10]

for p in pedidos:
    print("Pedido ID:",p.idPedido,"Estado:",p.estado.value)


# -------- INVENTARIO --------
print("\nINVENTARIOS")

inventario1 = Inventario()
inventario2 = Inventario()
inventario3 = Inventario()
inventario4 = Inventario()
inventario5 = Inventario()
inventario6 = Inventario()
inventario7 = Inventario()
inventario8 = Inventario()
inventario9 = Inventario()
inventario10 = Inventario()

inventarios = [inventario1,inventario2,inventario3,inventario4,inventario5,inventario6,inventario7,inventario8,inventario9,inventario10]

for i in range(len(inventarios)):
    print("Inventario creado número:",i+1)
