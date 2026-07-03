# ModernClothes

ModernClothes es un sistema de tienda online ejecutado desde la terminal. Permite navegar por un catálogo de ropa, agregar productos al carrito, calcular la factura y completar una compra ingresando los datos del cliente.

## Descripción

El proyecto simula el flujo básico de compra de una tienda de ropa. El usuario puede entrar al catálogo, elegir entre camisas/camisetas o shorts/pantalones, añadir varios productos al carrito y decidir si desea completar la compra o reiniciar el carrito.

La navegación se realiza con menús interactivos en consola usando la libreria `questionary`.

## Características

- Menú principal para entrar o salir del catálogo.
- Catálogo dividido en dos categorías:
  - Camisas/Camisetas
  - Shorts/Pantalones
- Cálculo automático de la factura.
- Opción para seguir agregando productos al carrito.
- Opción para volver al menú principal desde cada categoría.
- Confirmación de compra.
- Formulario de datos del cliente:
  - Nombre completo.
  - Número de celular.
  - Dirección de envío.
- Verificación de datos antes de finalizar.
- Opción para vaciar el carrito.

## Instalación

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd ModernClothes
```

2. Instala las dependencias:

```bash
pip install questionary prompt_toolkit
```

## Ejecución

Ejecuta el archivo principal:

```bash
python3 ModernClothes.py
```

## Notas

- El programa está pensado para ejecutarse en una terminal.
- En sistemas donde `clear` no funcione, puede que la pantalla no se limpie correctamente, pero el programa puede seguir ejecutándose.
- Si aparece un error de dependencia, instala nuevamente `questionary` y `prompt_toolkit`.
- Es recomendable instalar las librerias en un entorno de python por si acaso se puede romper algo en el sistema.

## Autor

Proyecto desarrollado como práctica de programación en python por Briam el mas pro.
