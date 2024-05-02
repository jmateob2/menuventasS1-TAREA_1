from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient, VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def create(self):
        validar = Valida()
        while True:
            borrarPantalla()
            print('\033c', end='')
            gotoxy(2,1);print(green_color+"*"*90+reset_color)
            gotoxy(30,2);print(blue_color+"Registro de Cliente")
            gotoxy(17,3);print(blue_color+Company.get_business_name())
            gotoxy(3,4);print("Cedula: ")
            dni=validar.cedula("Error: 10 digitos",23,4)
            json_file = JsonFile(path+'/archivos/clients.json')
            client = json_file.find("dni",dni)
            if client:
                gotoxy(35,6);print("Cliente ya existe")
                time.sleep(1)
            else: 
                break
        gotoxy(3,5);print("Nombre: ")
        first_name=validar.solo_letras("Error: Solo letras",23,5)
        gotoxy(3,6);print("Apellido:")
        last_name=validar.solo_letras("Error: Solo letras",23,6)
        tip_client=str(input("El cliente es VIP? (S/N): ")).upper()
        if tip_client=="S":
            tip=VipClient(first_name,last_name,dni)
            tip2=VipClient.getJson(tip)
        else:
            cards=str(input("el cliente tiene descuento? (S/N): ")).upper()
            if cards=="S": cards=True 
            else: cards=False
            tip=RegularClient(first_name,last_name,dni,cards)
            tip2=RegularClient.getJson(tip)
        gotoxy(15,9);print(red_color+"Esta seguro de agregar Cliente(s/n):")
        gotoxy(54,9);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10);print("😊 Cliente agragado exitosamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/clients.json')
            invoices = json_file.read()
            invoices.append(tip2)
            json_file = JsonFile(path+'/archivos/clients.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10);print("🤣 Cliente Cancelado 🤣"+reset_color)    
        time.sleep(2)
        
    def update(self):
        pass
    
    def delete(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(red_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Eliminar Ciente"+" "*35+"██")
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        gotoxy(2,3);print("Ingrese DNI del cliente a eliminar: ")
        gotoxy(2,3);dni= validar.cedula("Error: Cedula Incorrecta",40,3)
        clients = json_file.find("dni",dni)
        if clients:
            gotoxy(30,4);print(f"CLIENTE")
            gotoxy(2,5);print(green_color+"*"*90+reset_color)
            for cli in clients:
                if isinstance(cli["valor"],int):
                    gotoxy(2,6);print(purple_color+"CLIENTE VIP"+reset_color)
                    gotoxy(2,7);print(green_color+"█"*60+reset_color)
                    gotoxy(2,8);print(blue_color+"Cedula")
                    gotoxy(20,8);print("Nombre")
                    gotoxy(35,8);print("Apellido")
                    gotoxy(50,8);print("Valor"+reset_color)
                    gotoxy(2,9);print(green_color+"="*60+reset_color)
                    gotoxy(2,10);print(f"{cyan_color}{cli['dni']}")
                    gotoxy(20,10);print(f"{cli['nombre']}")
                    gotoxy(35,10);print(f"{cli['apellido']}")
                    gotoxy(50,10);print(f"{cli['valor']}{reset_color}")
                elif isinstance(cli["valor"],float):
                    gotoxy(2,6);print(purple_color+"CLIENTE REGULAR"+reset_color)
                    gotoxy(2,7);print(green_color+"█"*60+reset_color)
                    gotoxy(2,8);print(blue_color+"Cedula")
                    gotoxy(20,8);print("Nombre")
                    gotoxy(35,8);print("Apellido")
                    gotoxy(50,8);print("Valor"+reset_color)
                    gotoxy(2,9);print(green_color+"="*60+reset_color)
                    gotoxy(2,10);print(f"{cyan_color}{cli['dni']}")
                    gotoxy(20,10);print(f"{cli['nombre']}")
                    gotoxy(35,10);print(f"{cli['apellido']}")
                    gotoxy(50,10);print(f"{cli['valor']}{reset_color}")
            delete=str(input("Esta seguro de eliminar este cliente permanentemente(s/n): ")).lower()
            if delete.lower()=="s":
                clients = json_file.delete("dni",dni)
                print(clients)
            else:
                print("No se elimino al cliente VUELVA PRONTO")
            input("presione una tecla para regresar...")
        else:
            print("Cliente no existe VUelva pronto")
            time.sleep(2)
            
          
        #___________________________________________________
        # print('\033c', end='')
        # gotoxy(2,1);print(red_color+"█"*90)
        # gotoxy(2,2);print("██"+" "*34+"Eliminar Ciente"+" "*35+"██")
        # json_file = JsonFile(path+'/archivos/clients.json')
        # clients1 = json_file.read()
        # print("Clientes")
        # print(f"{"DNI".ljust(10)}   {"Nombre".ljust(9)}   {"Apellido".ljust(9)}   {"Valor".ljust(5)}"+reset_color)
        
        # for cli in clients1:
        #     print(green_color + f"{str(cli['dni']).ljust(10)}   {str(cli['nombre']).ljust(9)}   {str(cli['apellido']).ljust(9)}   {str(cli['valor']).ljust(5)}")
        # client= input("\tIngrese DNI del cliente a eliminar: ")
        # if client.isdigit():
        #     clients = json_file.delete("dni",client)
        #     print(clients)
        # else:
        #     print("No ingreso un DNI existente.... intentelo mas tarde...")
    
    def consult(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Cliente"+" "*33+"██")
        json_file = JsonFile(path+'/archivos/clients.json')
        gotoxy(2,2);invoices = json_file.read()
        gotoxy(2,3);print(yellow_color+"Ingrese la cedula del cliente que desea consultar:")
        gotoxy(2,3);invoice= validar.cedula("Error: Solo numeros",60,3)
        clients = json_file.find("dni",invoice)
        if clients:
            gotoxy(30,4);print(f"CLIENTE")
            gotoxy(2,5);print(green_color+"*"*90+reset_color)
            for cli in clients:
                if isinstance(cli["valor"],int):
                    gotoxy(2,6);print(purple_color+"CLIENTE VIP"+reset_color)
                    gotoxy(2,7);print(green_color+"█"*60+reset_color)
                    gotoxy(2,8);print(blue_color+"Cedula")
                    gotoxy(20,8);print("Nombre")
                    gotoxy(35,8);print("Apellido")
                    gotoxy(50,8);print("Valor"+reset_color)
                    gotoxy(2,9);print(green_color+"="*60+reset_color)
                    gotoxy(2,10);print(f"{cyan_color}{cli['dni']}")
                    gotoxy(20,10);print(f"{cli['nombre']}")
                    gotoxy(35,10);print(f"{cli['apellido']}")
                    gotoxy(50,10);print(f"{cli['valor']}{reset_color}")
                elif isinstance(cli["valor"],float):
                    gotoxy(2,6);print(purple_color+"CLIENTE REGULAR"+reset_color)
                    gotoxy(2,7);print(green_color+"█"*60+reset_color)
                    gotoxy(2,8);print(blue_color+"Cedula")
                    gotoxy(20,8);print("Nombre")
                    gotoxy(35,8);print("Apellido")
                    gotoxy(50,8);print("Valor"+reset_color)
                    gotoxy(2,9);print(green_color+"="*60+reset_color)
                    gotoxy(2,10);print(f"{cyan_color}{cli['dni']}")
                    gotoxy(20,10);print(f"{cli['nombre']}")
                    gotoxy(35,10);print(f"{cli['apellido']}")
                    gotoxy(50,10);print(f"{cli['valor']}{reset_color}")
            x=input("presione una tecla para regresar...")    
        else:
            print(red_color+f"{"DNI".ljust(10)}   {"Nombre".ljust(9)}   {"Apellido".ljust(9)}   {"Valor".ljust(5)}"+reset_color)    
            f=0          
            for cli in invoices:
                print(green_color + f"{str(cli['dni']).ljust(10)}   {str(cli['nombre']).ljust(9)}   {str(cli['apellido']).ljust(9)}   {str(cli['valor']).ljust(5)}")
                f+=1
            input(purple_color+"ESTA CEDULA NO EXISTE \nregresando.....") 

    
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class CrudProducts(ICrud):
    def create(self):
        validar = Valida()
        while True:
            borrarPantalla()
            print('\033c', end='')
            gotoxy(2,1);print(green_color+"*"*90+reset_color)
            gotoxy(30,2);print(blue_color+"Ingresar Producto")
            gotoxy(17,3);print(blue_color+Company.get_business_name())
            gotoxy(3,4);print("Producto: ")
            new_produc=validar.solo_letras("Error: Ingrese un producto",23,4).lower().capitalize()
            json_file = JsonFile(path+'/archivos/products.json')
            produ = json_file.find("descripcion",new_produc)
            if produ:
                gotoxy(35,6);print("Producto ya existe")
                time.sleep(1)

            else: 
                break
        gotoxy(3,5);print("Precio: ")
        precio=validar.solo_decimales("Error: Solo decimales",23,5)
        gotoxy(3,6);print("Stock: ")
        stock=validar.solo_numeros("Error: Solo numeros ",23,6)
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        if products:
            last_id = max(product["id"] for product in products)
            new_id = last_id + 1
        else:
            new_id = 1
        product=Product(new_id,new_produc,precio,stock)
        product=Product.getJson(product)
        gotoxy(15,9);print(red_color+"Esta seguro de grabar este producto(s/n):")
        gotoxy(59,9);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10);print("😊 Produco Grabado satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            products.append(product)
            json_file = JsonFile(path+'/archivos/products.json')
            json_file.save(products)
        else:
            gotoxy(20,10);print("🤣 Ingreso de producto Cancelada 🤣"+reset_color) 
            time.sleep(2)
    
    def update(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Actualización de Producto")
        # Solicitar el ID del producto que se desea actualizar
        product_id = int(input("Ingrese el ID del producto que desea actualizar: "))
        # Buscar el producto en el archivo JSON de productos
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        product_to_update = None
        for product in products:
            if product["id"] == product_id:
                product_to_update = product
                break
        
        if product_to_update:
    # Verificar que las claves existan antes de acceder a ellas
            if "descripcion" in product_to_update:
                print("Nombre:", product_to_update["descripcion"])
            if "precio" in product_to_update:
                print("Precio:", product_to_update["precio"])
            if "stock" in product_to_update:
                print("Stock:", product_to_update["stock"])
    
    # Solicitar la nueva información del producto
            nuevo_nombre = input("Ingrese el nuevo nombre del producto (deje vacío si no desea actualizar): ")
            nuevo_precio = input("Ingrese el nuevo precio del producto (deje vacío si no desea actualizar): ")
            nuevo_stock = input("Ingrese el nuevo stock del producto (deje vacío si no desea actualizar): ")

    # Actualizar la información del producto si se proporciona
            if nuevo_nombre:
                product_to_update["descripcion"] = nuevo_nombre
            if nuevo_precio:
                product_to_update["precio"] = float(nuevo_precio)
            if nuevo_stock:
                product_to_update["stock"] = int(nuevo_stock)

    # Guardar los cambios en el archivo JSON de productos
            json_file.save(products)
    
            print("Producto actualizado exitosamente.")
        else:
            print("No se encontró ningún producto con el ID proporcionado.")

        gotoxy(2,5);print(green_color+"*"*90+reset_color)
        
        gotoxy(8,13);input("Presione Enter para continuar...")
    
    def delete(self):
        validar=Valida()
        print('\033c', end='')
        gotoxy(2,1);print(red_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Eliminar producto"+" "*36+"██")
        json_file = JsonFile(path+'/archivos/products.json')
        produtc = json_file.read()
        gotoxy(2,3);print("Ingrese producto a eliminar: ")
        gotoxy(2,3);prod= int(validar.solo_numeros("Error: solo caracter",40,3))
        produtc = json_file.find("id",prod)
        if produtc:
            gotoxy(30,4);print(f"PRODUCTO")
            gotoxy(2,5);print(green_color+"*"*90+reset_color)
            for pro in produtc:
                ####################################
                gotoxy(2,7);print(green_color+"█"*60+reset_color)
                gotoxy(2,8);print(blue_color+"ID")
                gotoxy(20,8);print("PRODUCTO")
                gotoxy(35,8);print("PRECIO")
                gotoxy(50,8);print("STOCK"+reset_color)
                gotoxy(2,9);print(green_color+"="*60+reset_color)
                gotoxy(2,10);print(f"{cyan_color}{pro['id']}")
                gotoxy(20,10);print(f"{pro['descripcion']}")
                gotoxy(35,10);print(f"{pro['precio']}")
                gotoxy(50,10);print(f"{pro['stock']}{reset_color}")
                ################################
            delete=str(input("Esta seguro de eliminar este producto permanentemente(s/n): ")).lower()
            if delete.lower()=="s":
                product = json_file.delete("id",prod)
                print(product)
            else:
                print("No se elimino el producto VUELVA PRONTO")
            input("presione una tecla para regresar...")
        else:
            print("producto no existe VUelva pronto")
            time.sleep(2)
            
        #________________________________________________________
        # print('\033c', end='')
        # gotoxy(2,1);print(red_color+"█"*90)
        # gotoxy(2,2);print("██"+" "*34+"Eliminar producto"+" "*36+"██")
        # json_file = JsonFile(path+'/archivos/products.json')
        # invoices1 = json_file.read()
        
        # print(purple_color+"productos"+reset_color)
        # gotoxy(2,4);print(green_color+"id")
        # gotoxy(15,4);print("Descripcion")
        # gotoxy(30,4);print("Precio")
        # gotoxy(50,4);print("Stock"+reset_color)
        # d=1
        # for fac in invoices1:
        #     gotoxy(2,4+d);print(f"{blue_color}{fac['id']} ")
        #     gotoxy(15,4+d);print(f"{fac['descripcion']} ")
        #     gotoxy(30,4+d);print(f"{fac['precio']} ")
        #     gotoxy(50,4+d);print(f"{fac['stock']}")
        #     d+=1
        
        # invoice= input("\tIngrese id de producto a eliminar: ")
        # if invoice.isdigit():
        #     invoices = json_file.delete("id",int(invoice))
        #     print(invoices)
        # else:
        #     print("No ingreso el id correspondiente.... intentelo mas tarde..."+reset_color)
    
    def consult(self):
        validar=Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de productos"+" "*35+"██")
        json_file = JsonFile(path+'/archivos/products.json')
        produtc1 = json_file.read()
        gotoxy(2,3);print("Ingrese producto a consultar: ")
        gotoxy(2,3);prod= int(validar.solo_numeros("Error: solo caracter",40,3))
        produtc = json_file.find("id",prod)
        if produtc:
            gotoxy(30,4);print(f"PRODUCTO")
            gotoxy(2,5);print(green_color+"*"*90+reset_color)
            for pro in produtc:
                ####################################
                gotoxy(2,7);print(green_color+"█"*60+reset_color)
                gotoxy(2,8);print(blue_color+"ID")
                gotoxy(20,8);print("PRODUCTO")
                gotoxy(35,8);print("PRECIO")
                gotoxy(50,8);print("STOCK"+reset_color)
                gotoxy(2,9);print(green_color+"="*60+reset_color)
                gotoxy(2,10);print(f"{cyan_color}{pro['id']}")
                gotoxy(20,10);print(f"{pro['descripcion']}")
                gotoxy(35,10);print(f"{pro['precio']}")
                gotoxy(50,10);print(f"{pro['stock']}{reset_color}")
                ################################
                x=input("presione una tecla para continuar...")
        else:
            print("Producto no existente MOSTRANDO PRODUCTOS REGISTRADO")
            gotoxy(2,5);print(purple_color+"productos"+reset_color)
            gotoxy(2,6);print(green_color+"id")
            gotoxy(15,6);print("Descripcion")
            gotoxy(30,6);print("Precio")
            gotoxy(50,6);print("Stock"+reset_color)
            d=1
            for fac in produtc1:
                gotoxy(2,6+d);print(f"{blue_color}{fac['id']} ")
                gotoxy(15,6+d);print(f"{fac['descripcion']} ")
                gotoxy(30,6+d);print(f"{fac['precio']} ")
                gotoxy(50,6+d);print(f"{fac['stock']}")
                d+=1
            x=input("presione una tecla para continuar...") 
        
        # print('\033c', end='')
        # gotoxy(2,1);print(green_color+"█"*90)
        # gotoxy(2,2);print("██"+" "*34+"Consulta de productos"+" "*35+"██")
        # json_file = JsonFile(path+'/archivos/products.json')
        # invoices = json_file.read()
        # gotoxy(2,3);print(purple_color+"productos"+reset_color)
        # gotoxy(2,4);print(green_color+"id")
        # gotoxy(15,4);print("Descripcion")
        # gotoxy(30,4);print("Precio")
        # gotoxy(50,4);print("Stock"+reset_color)
        # d=1
        # for fac in invoices:
        #     gotoxy(2,4+d);print(f"{blue_color}{fac['id']} ")
        #     gotoxy(15,4+d);print(f"{fac['descripcion']} ")
        #     gotoxy(30,4+d);print(f"{fac['precio']} ")
        #     gotoxy(50,4+d);print(f"{fac['stock']}")
        #     d+=1
        # gotoxy(2,4+d);x=input("presione una tecla para continuar...")       
        # print("regresando.....")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(yellow_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni=validar.cedula("Error: cedula incorrecta",23,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line)
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)    
    
    def update(self):
        #____________________________________________________________________________
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(yellow_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Modificar Factura"+" "*35+"██")
        json_file = JsonFile(path+'/archivos/invoices.json')
        gotoxy(2,2);invoices1 = json_file.read()
        # gotoxy(2,3);print(purple_color+"Facturas"+reset_color)
        # f=0
        # for fac in invoices1:
        #         gotoxy(2,4+f);print(blue_color+f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}"+reset_color)
        #         f+=1
        gotoxy(2,3);print(green_color+"Ingrese Factura a MODIFICAR: "+reset_color)
        gotoxy(2,3);invoice = int(validar.solo_numeros("ERROR: solo numeros",30,3))
        
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoices = json_file.find("factura",invoice)
        if invoices:
            borrarPantalla()
            print('\033c', end='')
            gotoxy(30,1);print(yellow_color+f"Impresion de la Factura")
            gotoxy(2,2);print("*"*90+reset_color)
            for fac in invoices:
                follow="s"
                
                gotoxy(5,4);print(green_color+f"Factura#: {fac['factura']} {''*3} Fecha:{fac['Fecha']}")
                gotoxy(5,6);print(f"Comprador: {fac['cliente']}")
                gotoxy(66,4);print(f"Subtotal: {fac['subtotal']}")
                gotoxy(66,5);print(f"Decuento: {fac['descuento']}")
                gotoxy(66,6);print(f"Iva     : {fac['iva']}")
                gotoxy(66,7);print(f"Total   : {fac['total']}")
                gotoxy(2,8);print(purple_color+"*"*90+reset_color) 
                gotoxy(24,9);print(blue_color+"Articulo") 
                gotoxy(38,9);print("Precio") 
                gotoxy(48,9);print("Cantidad") 
                gotoxy(58,9);print("Subtotal") 
                gotoxy(70,9);print("s->para Modificar)"+reset_color)
                d=1
                iva_percentage = 0.12
                discount_percentage = 0.10
                #new_quantity = 0
                updated_details=[]
                new_subtotal=0
                #l=1
                for det in fac['detalle']:
                    d=+1
                    gotoxy(24,9+d);print(cyan_color+det['poducto']) 
                    gotoxy(38,9+d);print(det['precio']) 
                    gotoxy(48,9+d);print(det['cantidad']) 
                    gotoxy(53,9+d);qyt=int(validar.solo_numeros2("Error:Solo numeros",53,9+d))
                    gotoxy(58,9+d);print(qyt*det['precio'])
                    gotoxy(74,9+d);follow=input(reset_color) or "s" 
                    gotoxy(76,9+d);print(green_color+"✔"+reset_color)
                    if follow.lower()=="s":
                        if qyt > 0:
                            det["cantidad"] = qyt
                            updated_details.append(det)
                            new_subtotal += det["precio"] * det["cantidad"]                                
                    else:
                        updated_details.append(det)
                        new_subtotal += det["precio"] * det["cantidad"]                                  
                if updated_details==[]:    
                    invoices = json_file.delete("factura",int(invoice))
                    print(red_color+"Factura eliminada al quitar todos los productos"+reset_color)
                else:
                    fac['detalle'] =  updated_details
                    fac["subtotal"] = round(new_subtotal,2)
                    fac["descuento"] = round((new_subtotal * discount_percentage),2)
                    fac["iva"] = round(((new_subtotal - (new_subtotal * discount_percentage)) * iva_percentage),2)
                    fac["total"] = round((new_subtotal - (new_subtotal * discount_percentage) + ((new_subtotal - (new_subtotal * discount_percentage)) * iva_percentage)),2)   
                    #print(fac)
                    #print(invoices[0])
                    empty_invoice=[]
                    c=0
                    for fac2 in invoices1:
                        c+=1
                        if invoice==c:  
                            empty_invoice.append(fac)
                        else:
                                empty_invoice.append(fac2)      
                    json_file.save(empty_invoice)               
        else: 
            gotoxy(2,3);print(purple_color+"Facturas"+reset_color)
            f=0
            for fac in invoices1:
                    gotoxy(2,4+f);print(blue_color+f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}"+reset_color)
                    f+=1  
            print(red_color+"NO SE LOGRO REEMBOLSAR \nINTENTELO MAS TARDE"+reset_color)
            time.sleep(3)
        #___________________________________________________________________________________________
        
        
    def delete(seft):
        validar=Valida()
        print('\033c', end='')
        gotoxy(2,1);print(red_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Eliminar Factura"+" "*35+"██"+reset_color)
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoices1 = json_file.read()
        gotoxy(2,3);print(green_color+"Ingrese Factura a MODIFICAR: "+reset_color)
        gotoxy(2,3);invoice = int(validar.solo_numeros("ERROR: solo numeros",30,3))
        invoices=json_file.find("factura",invoice)
        if invoices:
            gotoxy(2,5);print(green_color+"*"*90+reset_color)
            gotoxy(30,6);print(purple_color+f"Factura#{invoice}")
            for factura in invoices:
                #print(f"Fecha: {factura['Fecha']}\tcliente: {factura['cliente']}")
                #print(f"subtotal: {factura['subtotal']}\tdescuento: {factura['descuento']}")
                #print(f"iva: {factura['iva']}\ttotal: {factura['total']}")
                gotoxy(5,8);print(f"cliente: {factura['cliente']} {' '*3} Fecha: {factura['Fecha']}")
                gotoxy(66,8);print(f"Subtotal:{factura['subtotal']}")
                gotoxy(66,9);print(f"Decuento:{factura['descuento']}")
                gotoxy(66,10);print(f"Iva     :{factura['iva']}")
                gotoxy(66,11);print(f"Total   :{factura['total']}"+reset_color)
                gotoxy(30,12);print(red_color+"Detalles")
                gotoxy(12,13);print("Producto") 
                gotoxy(38,13);print("Precio") 
                gotoxy(48,13);print("Cantidad"+reset_color)
                x=1
                for detalle in factura['detalle']:
                    gotoxy(12,13+x);print(blue_color+f"{detalle['poducto']}") 
                    gotoxy(38,13+x);print(f"{detalle['precio']}") 
                    gotoxy(48,13+x);print(f"{detalle['cantidad']}")
                    x+=1
            delete=input(red_color+"Esta seguro de querer eliminar esta factura(s/n):"+reset_color)
            if delete.lower()=="s":
                invoices = json_file.delete("factura",invoice)
                print(invoices)
            else:
                print(purple_color+"Se arrenpitio de eliminar que TROOL"+reset_color)
                time.sleep(3)
        else:
            print(red_color+"La factura que ingreso no existe")
            print(purple_color+"Facturas"+reset_color)
            print(blue_color+f"{"FACTURA".ljust(8)}   {"FECHA".ljust(13)}   {"CLIENTE".ljust(15)}   {"TOTAL".ljust(6)}"+reset_color)
            for fac in invoices1:
                print(cyan_color+f"{str(fac['factura']).ljust(8)}   {str(fac['Fecha']).ljust(13)}   {str(fac['cliente']).ljust(15)}   {str(fac['total']).ljust(6)}"+reset_color)
            x=input("Presione enter para continuar....")   
    
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Factura"+" "*35+"██")
        gotoxy(2,4);invoice= input(yellow_color+"Ingrese Factura: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            #print(f"Impresion de la Factura#{invoice}")
            if invoices:   
                gotoxy(2,5);print(green_color+"*"*90+reset_color)
                gotoxy(30,6);print(purple_color+f"Factura#{invoice}")
                for factura in invoices:
                    #print(f"Fecha: {factura['Fecha']}\tcliente: {factura['cliente']}")
                    #print(f"subtotal: {factura['subtotal']}\tdescuento: {factura['descuento']}")
                    #print(f"iva: {factura['iva']}\ttotal: {factura['total']}")
                    gotoxy(5,8);print(f"cliente: {factura['cliente']} {' '*3} Fecha: {factura['Fecha']}")
                    gotoxy(66,8);print(f"Subtotal:{factura['subtotal']}")
                    gotoxy(66,9);print(f"Decuento:{factura['descuento']}")
                    gotoxy(66,10);print(f"Iva     :{factura['iva']}")
                    gotoxy(66,11);print(f"Total   :{factura['total']}"+reset_color)
                    gotoxy(30,12);print(red_color+"Detalles")
                    gotoxy(12,13);print("Producto") 
                    gotoxy(38,13);print("Precio") 
                    gotoxy(48,13);print("Cantidad"+reset_color)
                    x=1
                    for detalle in factura['detalle']:
                        gotoxy(12,13+x);print(blue_color+f"{detalle['poducto']}") 
                        gotoxy(38,13+x);print(f"{detalle['precio']}") 
                        gotoxy(48,13+x);print(f"{detalle['cantidad']}")
                        x+=1
                        #print(f"{detalle['poducto']}\t\t{detalle['precio']}\t\t{detalle['cantidad']}")
            else:
                print(red_color+"Factura no existe"+reset_color)        
        else:    
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices1 = json_file.read()
            print(red_color+"La factura que ingreso no existe")
            print(purple_color+"Facturas"+reset_color)
            print(blue_color+f"{"FACTURA".ljust(8)}   {"FECHA".ljust(13)}   {"CLIENTE".ljust(15)}   {"TOTAL".ljust(6)}"+reset_color)
            for fac in invoices1:
                print(cyan_color+f"{str(fac['factura']).ljust(8)}   {str(fac['Fecha']).ljust(13)}   {str(fac['cliente']).ljust(15)}   {str(fac['total']).ljust(6)}"+reset_color)
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), invoices1,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices1))
            total_client = list(filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices1))
            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            print("filter cliente: ",total_client)
            print(f"map Facturas:{totales_map}")
            print(f"              max Factura:{max_invoice}")
            print(f"              min Factura:{min_invoice}")
            print(f"              sum Factura:{round(tot_invoices,2)}")
            print(f"              reduce Facturas:{suma}")
        x=input(green_color+"presione una tecla para continuar..."+reset_color)    

#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu(red_color+"Menu Facturacion"+reset_color,[purple_color+"1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla() 
            clients=CrudClients()   
            menu_clients = Menu(blue_color+"Menu Cientes"+reset_color,[cyan_color+"1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                clients.create()
            elif opc1 == "2":
                clients.update()
            elif opc1 == "3":
                clients.delete()
                time.sleep(2)
            elif opc1 == "4":
                clients.consult()
            #print("Regresando al menu Clientes...")
            # time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()   
            product=CrudProducts() 
            menu_products = Menu(blue_color+"Menu Productos"+reset_color,[cyan_color+"1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                product.create()
            elif opc2 == "2":
                product.update()
            elif opc2 == "3":
                product.delete()
            elif opc2 == "4":
                product.consult()
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu(blue_color+"Menu Ventas"+reset_color,[cyan_color+"1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
                time.sleep(2)
                
                
            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
                
            elif opc3 == "3":
                sales.update()
                time.sleep(2)
                
            
            elif opc3 == "4":
                sales.delete()
                time.sleep(2)
                
     
    print("Regresando al menu Principal...")
    # time.sleep(2)            

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()

