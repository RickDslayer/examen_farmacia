import json

def guardar(datos):
    with open("sucursales.json","w") as archivo:
        json.dump(datos,archivo,indent=4)

def cargar():
    with open("sucursales.json","r") as archivo:
        return json.load(archivo) 

sucursales = cargar()

def crear_registro(ID,name,addres,cellphone,ID_manager,):
    buscar = str(ID)
    if buscar in sucursales:
        print(f"el codigo: {buscar} ya existe")
    else:
        sucursales[buscar] = {"nombre":name,"direccion":addres,"telefono":cellphone,"ID_gerente":ID_manager}
        guardar(sucursales)
        print(f"la sucursal {name} fue registrada con exito")

def eliminar_sucursal(ID):
    buscar = str(ID)
    if buscar in sucursales:
        del sucursales[ID]

def editar_sucursal(ID):
    buscar = str(ID)
    if buscar in sucursales:
        new_name = str(input("ingrese el nuevo nombre de la sucursal (si es el mismo vuelva a escribirlo):"))
        new_addres = str(input("ingrese la nueva direccion (si es el mismo vuelva a escribirlo): "))
        new_cellphone = str(input("ingrese el nuevo telefono (si es el mismo vuelva a escribirlo): "))
        new_IDmanager = str(input("ingrese la nueva ID del gerente o responsable (si es el mismo vuelva a escribirlo): "))
        new_sucursal = sucursales[ID] = {"nombre":new_name,"direccion":new_addres,"telefono":new_cellphone,"ID_gerente":new_IDmanager}
        guardar(new_sucursal)
        print(f"la sucursal {new_name} fue editada exitosamente")
    else:
        print(f"no existe la sucursal con el ID: {ID}")