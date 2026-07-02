import os
import time
import questionary


Factura = 0

while True:
    os.system("clear")
    print("|========================================|")
    print("| *****Bienvenido a ModernClothes***** |")
    print("|========================================|")
    time.sleep(0.3)
    print("¿Quieres acceder al catalogo Online?")
    print("|" + "-" * 34 + "|")
    time.sleep(0.3)
    
    Confirmacion = questionary.select(
        "Responda: Si/No",
        choices=["Si", "No"],
        instruction="(Use las flechas para seleccionar)"
    ).ask()
    
    time.sleep(0.3)
    os.system("clear")
    
    if Confirmacion in ["Si", "si", "SI"]:
        Salir2 = 0
        while Salir2 == 0:
            print("|========================================|")
            print("|****Bienvenido al catalogo Online****|")
            print("|========================================|")
            print("Eliga que tipo de prenda desea:")
            time.sleep(0.3)
            
            Prendas = questionary.select(
                "Selecciona una categoría:",
                choices=["Camisas/Camisetas", "Shorts/Pantalones", "Salir del Sistema"],
                instruction="(Use las flechas para seleccionar y enter para confirmar)"
            ).ask()
            
            os.system("clear")
            
            # SECCION CAMISAS Y CAMISETAS
            if Prendas in ["1", "Camisas", "camisas", "Camisetas", "camisetas", "Camisas/Camisetas"]:
                Rproductos = "Si"
                print("|========================================|")
                print("|Eliga que tipo de Camisa desea:|")
                print("|========================================|")
                time.sleep(0.3)
                
                Camisa = questionary.select(
                    "Selecciona una opción:",
                    choices=[
                        "Tank Top........3.00$",
                        "T_Shirt.........5.00$",
                        "Polo Shirt......7.00$",
                        "Dress Shirt....10.00$",
                        "Jacket.........15.00$",
                        "Volver al Menu Principal"
                    ],
                    instruction="(Use las flechas para seleccionar)"
                ).ask()
                
                os.system("clear")
                
                if "Tank Top" in Camisa:
                    Factura = Factura + 3.00
                    print("|========================================|")
                    print(f" - Has Agregado (Tank Top) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "T_Shirt" in Camisa:
                    Factura = Factura + 5.00
                    print("|========================================|")
                    print(f" - Has Agregado (T_Shirt) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Polo" in Camisa:
                    Factura = Factura + 7.00
                    print("|========================================|")
                    print(f" - Has Agregado (Polo Shirt) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Dress" in Camisa:
                    Factura = Factura + 10.00
                    print("|========================================|")
                    print(f" - Has Agregado (Dress Shirt) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Jacket" in Camisa:
                    Factura = Factura + 15.00
                    print("|========================================|")
                    print(f" - Has Agregado (Jacket) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Volver" in Camisa:
                    os.system("clear")
                    time.sleep(0.3)
                    print("|========================================|")
                    print("|====(Has Salido al Menu Principal)====|")
                    print("|========================================|")
                    time.sleep(0.3)
                    os.system("clear")
                    Rproductos = "Si"
                
                else:
                    os.system("clear")
                    time.sleep(0.3)
                    print("|========================================|")
                    print("| *********Respuesta Invalida*********|")
                    print("| *Redirigiendo a la pantalla principal*|")
                    print("|========================================|")
                    time.sleep(0.7)
                    os.system("clear")
                    Rproductos = "Si"
            
            # SECCIÓN SHORTS Y PANTALONES
            elif Prendas in ["2", "Shorts", "shorts", "Pantalones", "pantalones", "Shorts/Pantalones"]:
                Rproductos = "Si"
                
                time.sleep(0.3)
                
                Shortss = questionary.select(
                    "Selecciona una opción:",
                    choices=[
                        "Bermuda Short...3.00$",
                        "Running Short...5.00$",
                        "Cargo Short....10.00$",
                        "Denim Short....15.00$",
                        "Baggy Short....20.00$",
                        "Volver al Menu Principal"
                    ],
                    instruction="(Use las flechas para seleccionar)"
                ).ask()
                
                os.system("clear")
                
                if "Bermuda" in Shortss:
                    Factura = Factura + 3.00
                    print("|========================================|")
                    print(f" - Has Agregado (Bermuda Short) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Running" in Shortss:
                    Factura = Factura + 5.00
                    print("|========================================|")
                    print(f" - Has Agregado (Running Short) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Cargo" in Shortss:
                    Factura = Factura + 10.00
                    print("|========================================|")
                    print(f" - Has Agregado (Cargo Short) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Denim" in Shortss:
                    Factura = Factura + 15.00
                    print("|========================================|")
                    print(f" - Has Agregado (Denim Short) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Baggy" in Shortss:
                    Factura = Factura + 20.00
                    print("|========================================|")
                    print(f" - Has Agregado (Baggy Short) al Carrito, Su Factura es: {Factura:.2f}$")
                    time.sleep(0.3)
                    
                    Rproductos = questionary.select(
                        "Deseas añadir mas productos a tu carrito:",
                        choices=["Si", "No"],
                        instruction="(Use las flechas para seleccionar)"
                    ).ask()
                    
                    if Rproductos in ["Si", "SI", "si"]:
                        os.system("clear")
                        print("|========================================|")
                        print("=(Redirigiendo a la pantalla Principal)=")
                        print("|========================================|")
                        time.sleep(0.3)
                        os.system("clear")
                        Salir2 = 0
                
                elif "Volver" in Shortss:
                    os.system("clear")
                    time.sleep(0.3)
                    print("|========================================|")
                    print("|====(Has Salido al Menu Principal)====|")
                    print("|========================================|")
                    time.sleep(0.3)
                    os.system("clear")
                    Rproductos = "Si"
                
                else:
                    os.system("clear")
                    time.sleep(0.3)
                    print("|========================================|")
                    print("| *********Respuesta Invalida*********|")
                    print("| *Redirigiendo a la pantalla principal*|")
                    print("|========================================|")
                    time.sleep(0.7)
                    os.system("clear")
                    Rproductos = "Si"
            
            else:
                time.sleep(0.3)
                print("|========================================|")
                print("| *****Desea Realmente Salir?****** |")
                print("|========================================|")
                time.sleep(0.8)
                
                ConfSalida = questionary.select(
                    "¿Desea vaciar carrito y salir?",
                    choices=["Si", "No"],
                    instruction="(Use las flechas para seleccionar)"
                ).ask()
                
                if ConfSalida in ["Si", "si", "SI"]:
                    os.system("clear")
                    print("|========================================|")
                    print("|//////(Has Salido del Sistema)//////|")
                    print("|========================================|")
                    time.sleep(0.7)
                    os.system("clear")
                    print("|========================================|")
                    print("|//////(Reiniciando Carrito)//////|")
                    print("|========================================|")
                    Factura = 0
                    time.sleep(0.7)
                    os.system("clear")
                    Salir2 = 1
                else:
                    os.system("clear")
            
            # PROCESAR 
            if Rproductos == "No":
                os.system("clear")
                print("|========================================|")
                print("|**********Su factura es de:***********|")
                time.sleep(0.3)
                print(f"|************* {Factura:.2f}$ ****************|")
                print("|" + "-" * 34 + "|")
                time.sleep(0.3)
                
                Respuesta2 = questionary.select(
                    "Desea completar la compra:",
                    choices=["Si", "No"],
                    instruction="(Use las flechas para seleccionar)"
                ).ask()
                
                Salir3 = 0
                while Salir3 == 0:
                    if Respuesta2 in ["Si", "si", "SI"]:
                        Salir3 = 1
                        os.system("clear")
                        print("|========================================|")
                        print("|Perfecto Ingrese los siguientes datos para confirmar:|")
                        print("|========================================|")
                        time.sleep(0.3)
                        
                        print("|***************************************************|")
                        Nombre = questionary.text(
                            "1.Nombre Completo:"
                        ).ask()
                        
                        print("|***************************************************|")
                        NummCell = questionary.text(
                            "2.Numero de Celular:"
                        ).ask()
                        
                        print("|***************************************************|")
                        DirecEnvio = questionary.text(
                            "3.Direccion de Envio:"
                        ).ask()
                        
                        time.sleep(0.7)
                        os.system("clear")
                        print("|========================================|")
                        print("|Verifique si los siguientes datos son Correctos:|")
                        print(f"|Nombre: {Nombre}|")
                        time.sleep(0.3)
                        print(f"|Numero de Celular: {NummCell}|")
                        time.sleep(0.3)
                        print(f"|Direccion: {DirecEnvio}|")
                        print("|========================================|")
                        print("|Si cometio algun tipo de error al ingresar los datos|")
                        print("|puede cambiarlo ahora.|")
                        
                        ConfDatos = questionary.select(
                            "Desea modificar la informacion ingresada:",
                            choices=["Si", "No"],
                            instruction="(Use las flechas para seleccionar)"
                        ).ask()
                        
                        if ConfDatos in ["Si", "si", "SI"]:
                            os.system("clear")
                            time.sleep(0.3)
                            print("|========================================|")
                            print("| *******************Redirigiendo*********************|")
                            print("|========================================|")
                            time.sleep(0.7)
                            Salir3 = 0
                            os.system("clear")
                        
                        elif ConfDatos in ["No", "no", "NO"]:
                            os.system("clear")
                            time.sleep(0.3)
                            print("|========================================|")
                            print(f"|Perfecto,{Nombre} su pedido llegara en un plazo de:|")
                            print(f"| - 3 a 5 dias hábiles, a su direccion:{DirecEnvio}|")
                            print(f"|Cualquier notificacion o inconveniente se le|")
                            print(f"|comunicara a su numero:{NummCell}|")
                            print("|========================================|")
                            time.sleep(0.5)
                            print("|========================================|")
                            print("| ***Sus operaciones han finalizado***|")
                            time.sleep(0.3)
                            print("| ******Gracias por Visitarnos*******|")
                            print("|========================================|")
                            print()
                            input("Presione Enter para salir del sistema...")
                            os.system("clear")
                            break
                            Salir = 1
                            Salir2 = 1
                            Salir3 = 1
                    
                    elif Respuesta2 in ["No", "no", "NO"]:
                        os.system("clear")
                        time.sleep(0.3)
                        print("|========================================|")
                        
                        Respuesta3 = questionary.select(
                            "Desea vaciar su carrito y volver al menu principal:",
                            choices=["Si", "No"],
                            instruction="(Use las flechas para seleccionar)"
                        ).ask()
                        
                        if Respuesta3 in ["Si", "si", "SI"]:
                            time.sleep(0.3)
                            os.system("clear")
                            Factura = 0
                            Salir2 = 0
                            Salir3 = 1
                        
                        elif Respuesta3 in ["no", "No", "NO"]:
                            os.system("clear")
                            time.sleep(0.3)
                            print("|========================================|")
                            print("| ***Sus operaciones han finalizado***|")
                            time.sleep(0.3)
                            print("| ******Gracias por Visitarnos*******|")
                            print("|========================================|")
                            Salir = 1
                            Salir2 = 1
                            Salir3 = 1
                
                Rproductos = "Si"
    
    elif Confirmacion in ["No", "no", "NO"]:
        print("|========================================|")
        print("| ***Sus operaciones han finalizado***|")
        time.sleep(0.3)
        print("| ******Gracias por Visitarnos*******|")
        print("|========================================|")
        break
        