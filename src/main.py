
# =========================================================
# IMPORTACIÓN
# =========================================================

from pathlib import Path


# =========================================================
# LECTURA DEL ARCHIVO DE PRODUCTOS
# =========================================================

# Busca el archivo de productos desde la raíz del proyecto.
archivo = Path("datos/productos.txt")

# Lee el contenido y lo separa en líneas individuales.
lineas = archivo.read_text(encoding="utf-8").splitlines()


# =========================================================
# MOSTRAR EL INVENTARIO
# =========================================================

# Muestra el título del inventario.
print("=== Inventario Tienda Don Pedro ===")

# Omite las dos primeras líneas: el encabezado y la línea vacía.
productos = lineas[2:]

# Recorre y muestra cada producto.
for linea in productos:
    print("-", linea)


# =========================================================
# CALCULAR LA CANTIDAD Y EL VALOR DEL INVENTARIO
# =========================================================

# Cuenta cuántos productos hay en la lista.
total_productos = len(productos)

# Inicializa el valor total del inventario en cero.
valor_inventario = 0

# Recorre cada producto para obtener y sumar su precio.
for producto in productos:

    # Separa el nombre del producto y su precio.
    nombre, precio = producto.split(" - $")

    # Elimina los puntos de los precios y los convierte
    # en números enteros para poder sumarlos.
    precio_numerico = int(precio.replace(".", ""))

    # Suma el precio al valor total del inventario.
    valor_inventario += precio_numerico


# =========================================================
# MOSTRAR LOS RESULTADOS
# =========================================================

# Muestra la cantidad de productos encontrados.
print("Total de productos:", total_productos)

# Muestra el valor total del inventario.
print(f"Valor del inventario: ${valor_inventario}")
