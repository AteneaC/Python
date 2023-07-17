class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)

    def vender_producto(self, id):
        if id >= 0 and id < len(self.productos):
            producto = self.productos.pop(id)
            producto.print_info()
        else:
            print("No se encontró ningún producto con el ID proporcionado.")

    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, False)


class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100

    def print_info(self):
        print("Nombre: ", self.nombre)
        print("Categoría: ", self.categoria)
        print("Precio: $", self.precio)

# Crear una tienda
tienda = Tienda("Mi Tienda")

# Crear productos
producto1 = Producto("Camiseta", 25.99, "Ropa")
producto2 = Producto("Zapatos", 59.99, "Calzado")
producto3 = Producto("Bolso", 39.99, "Accesorios")

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Vender un producto por su ID
tienda.vender_producto(1)  # Vende el segundo producto de la lista

# Aumentar el precio de todos los productos en un 10%
tienda.inflacion(10)

# Aplicar descuento del 20% a los productos de la categoría "Ropa"
tienda.hacer_liquidacion("Ropa", 20)
