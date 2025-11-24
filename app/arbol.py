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
            print("✗ Producto no encontrado")
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



