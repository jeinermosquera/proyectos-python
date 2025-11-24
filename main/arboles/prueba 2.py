"""
APLICACIÓN REAL: Sistema de Inventario de Productos
Con menú interactivo y visualización gráfica del árbol BST
"""

import networkx as nx
import matplotlib.pyplot as plt

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        """Muestra la información completa del producto de forma legible"""
        return f"[{self.codigo}] {self.nombre} - ${self.precio} (Stock: {self.stock})"


class NodoProducto:
    def __init__(self, producto):
        self.producto = producto
        self.izquierdo = None
        self.derecho = None


class SistemaInventario:
    def __init__(self):
        self.raiz = None
    
    def agregar_producto(self, codigo, nombre, precio, stock):
        """Agrega un producto al inventario"""
        producto = Producto(codigo, nombre, precio, stock)
        if self.raiz is None:
            self.raiz = NodoProducto(producto)
        else:
            self._insertar(self.raiz, producto)
        print(f"✓ Producto agregado: {producto.mostrar_info()}")
    
    def _insertar(self, nodo, producto):
        if producto.codigo < nodo.producto.codigo:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoProducto(producto)
            else:
                self._insertar(nodo.izquierdo, producto)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoProducto(producto)
            else:
                self._insertar(nodo.derecho, producto)
    
    def buscar_producto(self, codigo):
        """Busca un producto por código"""
        return self._buscar(self.raiz, codigo)
    
    def _buscar(self, nodo, codigo):
        if nodo is None:
            return None
        if nodo.producto.codigo == codigo:
            return nodo.producto
        elif codigo < nodo.producto.codigo:
            return self._buscar(nodo.izquierdo, codigo)
        else:
            return self._buscar(nodo.derecho, codigo)
    
    def listar_productos(self):
        """Lista todos los productos ordenados por código"""
        productos = []
        self._recorrer_inorden(self.raiz, productos)
        return productos
    
    def _recorrer_inorden(self, nodo, productos):
        if nodo:
            self._recorrer_inorden(nodo.izquierdo, productos)
            productos.append(nodo.producto)
            self._recorrer_inorden(nodo.derecho, productos)
    
    def productos_por_precio(self, precio_min, precio_max):
        """Busca productos en un rango de precio"""
        productos = []
        self._buscar_por_precio(self.raiz, precio_min, precio_max, productos)
        return productos
    
    def _buscar_por_precio(self, nodo, precio_min, precio_max, productos):
        if nodo:
            self._buscar_por_precio(nodo.izquierdo, precio_min, precio_max, productos)
            if precio_min <= nodo.producto.precio <= precio_max:
                productos.append(nodo.producto)
            self._buscar_por_precio(nodo.derecho, precio_min, precio_max, productos)
    
    def actualizar_stock(self, codigo, cantidad):
        """Actualiza el stock de un producto"""
        producto = self.buscar_producto(codigo)
        if producto:
            producto.stock += cantidad
            print(f"✓ Stock actualizado: {producto.mostrar_info()}")
            return True
        print("✗ Producto no encontrado")
        return False
    
    def visualizar_arbol_grafico(self):
        """Genera una visualización gráfica del árbol usando NetworkX y Matplotlib"""
        if self.raiz is None:
            print("El árbol está vacío")
            return
        
        # Crear el grafo dirigido
        G = nx.DiGraph()
        pos = {}
        labels = {}
        
        # Construir el grafo y calcular posiciones
        self._construir_grafo(G, self.raiz, pos, labels, x=0, y=0, layer=1)
        
        # Configurar la figura
        plt.figure(figsize=(14, 8))
        plt.title("Árbol Binario de Búsqueda - Sistema de Inventario", 
                 fontsize=16, fontweight='bold', pad=20)
        
        # Dibujar el grafo
        nx.draw_networkx_nodes(G, pos, node_color='#4ECDC4', 
                              node_size=3000, alpha=0.9)
        nx.draw_networkx_edges(G, pos, edge_color='#95A5A6', 
                              arrows=True, arrowsize=20, 
                              arrowstyle='->', width=2)
        nx.draw_networkx_labels(G, pos, labels, font_size=9, 
                               font_weight='bold', font_color='white')
        
        plt.axis('off')
        plt.tight_layout()
        
        try:
            plt.savefig('arbol_inventario.png', dpi=300, bbox_inches='tight', 
                       facecolor='white')
            print("\n✓ Visualización guardada como 'arbol_inventario.png'")
            plt.show()
        except Exception as e:
            print(f"\n✗ Error al generar visualización: {e}")
    
    def _construir_grafo(self, G, nodo, pos, labels, x, y, layer, x_offset=None):
        """Construye el grafo recursivamente y calcula posiciones jerárquicas"""
        if nodo is None:
            return
        
        # Calcular offset horizontal basado en el nivel del árbol
        if x_offset is None:
            x_offset = 4 / layer
        
        # Agregar nodo al grafo
        node_id = nodo.producto.codigo
        G.add_node(node_id)
        pos[node_id] = (x, y)
        labels[node_id] = f"{nodo.producto.codigo}\n{nodo.producto.nombre}"
        
        # Procesar hijo izquierdo
        if nodo.izquierdo:
            hijo_izq = nodo.izquierdo.producto.codigo
            G.add_edge(node_id, hijo_izq)
            self._construir_grafo(G, nodo.izquierdo, pos, labels, 
                                 x - x_offset, y - 1, layer + 1, x_offset / 2)
        
        # Procesar hijo derecho
        if nodo.derecho:
            hijo_der = nodo.derecho.producto.codigo
            G.add_edge(node_id, hijo_der)
            self._construir_grafo(G, nodo.derecho, pos, labels, 
                                 x + x_offset, y - 1, layer + 1, x_offset / 2)


def cargar_productos_prueba(inventario):
    """Carga 10 productos de prueba en el inventario"""
    productos_prueba = [
        (50, "Laptop", 1200.00, 15),
        (30, "Mouse", 25.50, 50),
        (70, "Monitor", 350.00, 20),
        (20, "Teclado", 45.00, 30),
        (40, "Webcam", 80.00, 25),
        (60, "Auriculares", 65.00, 40),
        (80, "Impresora", 200.00, 10),
        (10, "Cable HDMI", 15.00, 100),
        (35, "Hub USB", 30.00, 35),
        (75, "Micrófono", 120.00, 18)
    ]
    
    print("\n" + "="*50)
    print("CARGANDO 10 PRODUCTOS DE PRUEBA...")
    print("="*50)
    
    for codigo, nombre, precio, stock in productos_prueba:
        inventario.agregar_producto(codigo, nombre, precio, stock)
    
    print(f"\n{'='*50}")
    print(f"✓ Se cargaron {len(productos_prueba)} productos exitosamente")
    print(f"{'='*50}")


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("SISTEMA DE INVENTARIO")
    print("="*50)
    print("1. Agregar producto(s)")
    print("2. Buscar producto por código")
    print("3. Listar todos los productos")
    print("4. Buscar por rango de precio")
    print("5. Actualizar stock")
    print("6. Ver estructura del árbol (gráfico)")
    print("7. Cargar 10 productos de prueba")
    print("8. Salir")
    print("="*50)



    inventario = SistemaInventario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                # Agregar producto(s)
                print("\n--- AGREGAR PRODUCTO(S) ---")
                
                while True:
                    try:
                        cantidad = int(input("¿Cuántos productos desea agregar? "))
                        if cantidad > 0:
                            break
                        print("✗ Debe agregar al menos 1 producto.")
                    except ValueError:
                        print("✗ Debe ingresar un número válido. Intente de nuevo.")
                
                productos_agregados = 0
                
                for i in range(cantidad):
                    print(f"\n{'='*50}")
                    print(f"PRODUCTO {i+1} DE {cantidad} ({cantidad - i} restantes)")
                    print(f"{'='*50}")
                    
                    while True:
                        try:
                            codigo = int(input(f"Ingrese el CÓDIGO del producto {i+1}: "))
                            if inventario.buscar_producto(codigo):
                                print(f"✗ Este código ya existe. Ingrese uno diferente para el producto {i+1}.")
                                continue
                            break
                        except ValueError:
                            print(f"✗ Error: No puede ingresar letras en el código del producto {i+1}.")
                            print(f"   Debe ser un número entero. Intente de nuevo.")
                    
                    while True:
                        nombre = input(f"Ingrese el NOMBRE del producto {i+1}: ").strip()
                        if nombre:
                            break
                        print(f"✗ El nombre del producto {i+1} no puede estar vacío.")
                    
                    while True:
                        try:
                            precio = float(input(f"Ingrese el PRECIO del producto {i+1}: $"))
                            if precio > 0:
                                break
                            print(f"✗ El precio del producto {i+1} debe ser mayor a 0.")
                        except ValueError:
                            print(f"✗ Error: Precio inválido para el producto {i+1}. Debe ser un número.")
                    
                    while True:
                        try:
                            stock = int(input(f"Ingrese el STOCK del producto {i+1}: "))
                            if stock >= 0:
                                break
                            print(f"✗ El stock del producto {i+1} no puede ser negativo.")
                        except ValueError:
                            print(f"✗ Error: Stock inválido para el producto {i+1}. Debe ser un número entero.")
                    
                    inventario.agregar_producto(codigo, nombre, precio, stock)
                    productos_agregados += 1
                
                print(f"\n{'='*50}")
                print(f"✓ Se agregaron {productos_agregados} producto(s) exitosamente")
                print(f"{'='*50}")
            
            case "2":
                print("\n--- BUSCAR PRODUCTO ---")
                while True:
                    try:
                        codigo = int(input("Ingrese el código del producto: "))
                        producto = inventario.buscar_producto(codigo)
                        if producto:
                            print(f"\nProducto encontrado: {producto.mostrar_info()}")
                        else:
                            print("✗ Producto no encontrado")
                        break
                    except ValueError:
                        print("✗ Código inválido. Debe ser un número entero. Intente de nuevo.")
            
            case "3":
                print("\n--- INVENTARIO COMPLETO ---")
                productos = inventario.listar_productos()
                if productos:
                    for p in productos:
                        print(f"  {p.mostrar_info()}")
                else:
                    print("El inventario está vacío")
            
            case "4":
                print("\n--- BUSCAR POR RANGO DE PRECIO ---")
                
                while True:
                    try:
                        precio_min = float(input("Precio mínimo: $"))
                        if precio_min >= 0:
                            break
                        print("✗ El precio mínimo no puede ser negativo.")
                    except ValueError:
                        print("✗ Precio inválido. Debe ser un número. Intente de nuevo.")
                
                while True:
                    try:
                        precio_max = float(input("Precio máximo: $"))
                        if precio_max >= precio_min:
                            break
                        print(f"✗ El precio máximo debe ser mayor o igual a ${precio_min}")
                    except ValueError:
                        print("✗ Precio inválido. Debe ser un número. Intente de nuevo.")
                
                productos = inventario.productos_por_precio(precio_min, precio_max)
                if productos:
                    print(f"\nProductos entre ${precio_min} y ${precio_max}:")
                    for p in productos:
                        print(f"  {p.mostrar_info()}")
                else:
                    print("No se encontraron productos en ese rango")
            
            case "5":
                print("\n--- ACTUALIZAR STOCK ---")
                
                while True:
                    try:
                        codigo = int(input("Código del producto: "))
                        break
                    except ValueError:
                        print("✗ Código inválido. Debe ser un número entero. Intente de nuevo.")
                
                while True:
                    try:
                        cantidad = int(input("Cantidad a sumar/restar (use - para restar): "))
                        break
                    except ValueError:
                        print("✗ Cantidad inválida. Debe ser un número entero. Intente de nuevo.")
                
                inventario.actualizar_stock(codigo, cantidad)
            
            case "6":
                print("\n--- VISUALIZACIÓN DEL ÁRBOL (GRÁFICO) ---")
                inventario.visualizar_arbol_grafico()
            
            case "7":
                print("\n--- CARGAR PRODUCTOS DE PRUEBA ---")
                cargar_productos_prueba(inventario)
            
            case "8":
                print("\n¡Hasta luego!")
                break
            
            case _:
                print("✗ Opción inválida. Intente de nuevo.")
        
        input("\nPresione ENTER para continuar...")
