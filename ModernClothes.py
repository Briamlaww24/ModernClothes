import os
import time
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
import questionary
import Menus

Factura = 0
Camisa, Shorts = "", ""

os.system('clear')
Confirmacion = Menus.Menu_principal()
while True:
    os.system('clear')
    if Confirmacion == "Si":
        
        Prendas = Menus.Menu_catalogo()
        if Prendas == "1 - Camisas/Camisetas":
            Camisa, Factura = Menus.Menu_camisas(Camisa, Factura)
            if Camisa is None:
                continue

            Añadir = Menus.Menu_Camisa_Seleccionada(Camisa, Factura)
            if Añadir == "Si":
                pass
            elif Añadir == "No":
                Continuar = Menus.Menu_Factura(Factura)
                if Continuar == "Si":
                    Menus.Completar_compra()
                    break

                elif Continuar == "No":
                    Respuesta, Factura = Menus.Reinicio_del_Carrito(Factura)
                    
                    if Respuesta == "No":
                        break

        elif Prendas == "2 - Shorts/Pantalones":
            Shorts, Factura = Menus.Menu_pantalones(Shorts, Factura)
            if Shorts is None:
                continue

            Añadir = Menus.Menu_Pantalon_Seleccionado(Shorts, Factura)
            if Añadir == "Si":
                pass
            elif Añadir == "No":
                Continuar = Menus.Menu_Factura(Factura)
                if Continuar == "Si":
                    Menus.Completar_compra()
                    break

                elif Continuar == "No":
                    Respuesta, Factura = Menus.Reinicio_del_Carrito(Factura)
                    if Respuesta == "No":
                        break

        elif Prendas == "3 - ***(Salir del Sistema)***":
            Menus.Menu_salir()
            break

    elif Confirmacion == "No":
        Menus.Menu_salir()
        break
