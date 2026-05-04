import modulos.administracion as a
while True:
    print("menu")
    print("1. registrar nueva sucursal")
    print("2. editar sucursal")
    print("3. eliminar sucursal")
    print("4. visualizar sucursales")
    print("5. visualizar sucursales por nombre")
    opcion = str(input("escriba el numero de la opcion deseada: "))
    if opcion == "1":
        ID = str(input("ingrese la ID de la sucursal a registrar: "))
        name = str(input("ingrese el nombre de la sucursal a registrar: "))
        addres = str(input("ingrese la direccion de la sucursal a registrar: "))
        cellphone = str(input("ingrese el numero de telefono de la sucursal a registrar: "))
        ID_manager = str(input("ingrese la ID del gerente o responsable de la sucursal: "))
        a.crear_registro(ID,name,addres,cellphone,ID_manager)
    elif opcion == "2":
        ID = str(input("ingrese la ID de la sucursal a editar: "))
        a.editar_sucursal(ID)
    elif opcion == "3":
        ID = str(input("ingrese la ID de la sucursal a eliminar: "))
        a.eliminar_sucursal(ID)
    elif opcion == "4":
        sucursales = a.cargar()
        print(sucursales)
    elif opcion == "5":
        name = str(input("ingrese el nombre de la sucursal que desea buscar: "))
        a.buscar_sucursales(name)
