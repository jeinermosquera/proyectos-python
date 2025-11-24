import React, { useState } from 'react';
import { Plus, Trash2, RotateCcw, Package } from 'lucide-react';

// Clase para el nodo del árbol AVL
class AVLNode {
  constructor(producto) {
    this.producto = producto;
    this.height = 1;
    this.left = null;
    this.right = null;
  }
}

// Clase para el árbol AVL
class AVLTree {
  constructor() {
    this.root = null;
  }

  height(node) {
    return node ? node.height : 0;
  }

  balanceFactor(node) {
    return node ? this.height(node.left) - this.height(node.right) : 0;
  }

  updateHeight(node) {
    if (node) {
      node.height = Math.max(this.height(node.left), this.height(node.right)) + 1;
    }
  }

  rotateRight(y) {
    const x = y.left;
    const T2 = x.right;
    x.right = y;
    y.left = T2;
    this.updateHeight(y);
    this.updateHeight(x);
    return x;
  }

  rotateLeft(x) {
    const y = x.right;
    const T2 = y.left;
    y.left = x;
    x.right = T2;
    this.updateHeight(x);
    this.updateHeight(y);
    return y;
  }

  insert(node, producto) {
    if (!node) return new AVLNode(producto);

    if (producto.id < node.producto.id) {
      node.left = this.insert(node.left, producto);
    } else if (producto.id > node.producto.id) {
      node.right = this.insert(node.right, producto);
    } else {
      return node;
    }

    this.updateHeight(node);
    const balance = this.balanceFactor(node);

    // Rotación derecha
    if (balance > 1 && producto.id < node.left.producto.id) {
      return this.rotateRight(node);
    }

    // Rotación izquierda
    if (balance < -1 && producto.id > node.right.producto.id) {
      return this.rotateLeft(node);
    }

    // Rotación izquierda-derecha
    if (balance > 1 && producto.id > node.left.producto.id) {
      node.left = this.rotateLeft(node.left);
      return this.rotateRight(node);
    }

    // Rotación derecha-izquierda
    if (balance < -1 && producto.id < node.right.producto.id) {
      node.right = this.rotateRight(node.right);
      return this.rotateLeft(node);
    }

    return node;
  }

  add(producto) {
    this.root = this.insert(this.root, producto);
  }

  toArray(node = this.root, arr = []) {
    if (node) {
      this.toArray(node.left, arr);
      arr.push(node.producto);
      this.toArray(node.right, arr);
    }
    return arr;
  }
}
// 
// Componente para visualizar un nodo
const TreeNode = ({ node, x, y, parentX, parentY, level }) => {
  if (!node) return null;

  const horizontalSpacing = 120 / (level + 1);
  const verticalSpacing = 80;
  
  const leftX = x - horizontalSpacing;
  const leftY = y + verticalSpacing;
  const rightX = x + horizontalSpacing;
  const rightY = y + verticalSpacing;

  const balance = node.left && node.right 
    ? node.left.height - node.right.height 
    : node.left 
    ? node.left.height 
    : node.right 
    ? -node.right.height 
    : 0;

  return (
    <g>
      {parentX !== undefined && (
        <line
          x1={parentX}
          y1={parentY}
          x2={x}
          y2={y}
          stroke="#94a3b8"
          strokeWidth="2"
        />
      )}
      
      {node.left && (
        <TreeNode
          node={node.left}
          x={leftX}
          y={leftY}
          parentX={x}
          parentY={y}
          level={level + 1}
        />
      )}
      
      {node.right && (
        <TreeNode
          node={node.right}
          x={rightX}
          y={rightY}
          parentX={x}
          parentY={y}
          level={level + 1}
        />
      )}

      <circle
        cx={x}
        cy={y}
        r="28"
        fill={Math.abs(balance) > 1 ? "#fca5a5" : "#86efac"}
        stroke="#1e293b"
        strokeWidth="2"
      />
      
      <text
        x={x}
        y={y - 5}
        textAnchor="middle"
        fill="#1e293b"
        fontSize="12"
        fontWeight="bold"
      >
        {node.producto.id}
      </text>
      
      <text
        x={x}
        y={y + 8}
        textAnchor="middle"
        fill="#475569"
        fontSize="9"
      >
        ${node.producto.precio}
      </text>
      
      <circle
        cx={x + 22}
        cy={y - 22}
        r="8"
        fill="#3b82f6"
        stroke="#1e293b"
        strokeWidth="1"
      />
      <text
        x={x + 22}
        y={y - 19}
        textAnchor="middle"
        fill="white"
        fontSize="9"
        fontWeight="bold"
      >
        {balance}
      </text>
    </g>
  );
};

export default function AVLTreeVisualizer() {
  const [tree] = useState(() => new AVLTree());
  const [productos, setProductos] = useState([]);
  const [nuevoProducto, setNuevoProducto] = useState({ id: '', nombre: '', precio: '' });
  const [refreshKey, setRefreshKey] = useState(0);

  const productosIniciales = [
    { id: 15, nombre: 'Laptop', precio: 1200 },
    { id: 10, nombre: 'Mouse', precio: 25 },
    { id: 20, nombre: 'Teclado', precio: 80 },
    { id: 8, nombre: 'Monitor', precio: 300 },
    { id: 12, nombre: 'Webcam', precio: 60 },
    { id: 25, nombre: 'Auriculares', precio: 150 },
    { id: 5, nombre: 'USB', precio: 15 },
    { id: 30, nombre: 'SSD', precio: 200 },
    { id: 18, nombre: 'RAM', precio: 90 },
    { id: 22, nombre: 'GPU', precio: 500 }
  ];

  const agregarProductosIniciales = () => {
    productosIniciales.forEach(prod => {
      tree.add(prod);
    });
    setProductos(tree.toArray());
    setRefreshKey(prev => prev + 1);
  };

  const agregarProducto = () => {
    const id = parseInt(nuevoProducto.id);
    const precio = parseFloat(nuevoProducto.precio);

    if (!id || !nuevoProducto.nombre || !precio) {
      alert('Por favor completa todos los campos');
      return;
    }

    if (productos.some(p => p.id === id)) {
      alert('Ya existe un producto con ese ID');
      return;
    }

    const producto = { id, nombre: nuevoProducto.nombre, precio };
    tree.add(producto);
    setProductos(tree.toArray());
    setNuevoProducto({ id: '', nombre: '', precio: '' });
    setRefreshKey(prev => prev + 1);
  };

  const reiniciar = () => {
    tree.root = null;
    setProductos([]);
    setRefreshKey(prev => prev + 1);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 p-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2 flex items-center justify-center gap-3">
            <Package className="w-10 h-10" />
            Árbol AVL - Gestor de Productos
          </h1>
          <p className="text-blue-200">Visualización interactiva con auto-balanceo</p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-8">
          <div className="md:col-span-2 bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <h2 className="text-xl font-semibold text-white mb-4">Agregar Producto</h2>
            <div className="grid grid-cols-3 gap-4 mb-4">
              <input
                type="number"
                placeholder="ID"
                value={nuevoProducto.id}
                onChange={(e) => setNuevoProducto({ ...nuevoProducto, id: e.target.value })}
                className="px-4 py-2 rounded-lg bg-white/20 text-white placeholder-blue-200 border border-white/30 focus:outline-none focus:ring-2 focus:ring-blue-400"
              />
              <input
                type="text"
                placeholder="Nombre"
                value={nuevoProducto.nombre}
                onChange={(e) => setNuevoProducto({ ...nuevoProducto, nombre: e.target.value })}
                className="px-4 py-2 rounded-lg bg-white/20 text-white placeholder-blue-200 border border-white/30 focus:outline-none focus:ring-2 focus:ring-blue-400"
              />
              <input
                type="number"
                placeholder="Precio"
                value={nuevoProducto.precio}
                onChange={(e) => setNuevoProducto({ ...nuevoProducto, precio: e.target.value })}
                className="px-4 py-2 rounded-lg bg-white/20 text-white placeholder-blue-200 border border-white/30 focus:outline-none focus:ring-2 focus:ring-blue-400"
              />
            </div>
            <div className="flex gap-3">
              <button
                onClick={agregarProducto}
                className="flex-1 bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-2 rounded-lg hover:from-blue-600 hover:to-blue-700 transition-all flex items-center justify-center gap-2 font-medium"
              >
                <Plus className="w-5 h-5" />
                Agregar Uno
              </button>
              <button
                onClick={agregarProductosIniciales}
                className="flex-1 bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-2 rounded-lg hover:from-green-600 hover:to-green-700 transition-all flex items-center justify-center gap-2 font-medium"
              >
                <Package className="w-5 h-5" />
                Agregar 10 Productos
              </button>
              <button
                onClick={reiniciar}
                className="bg-gradient-to-r from-red-500 to-red-600 text-white px-6 py-2 rounded-lg hover:from-red-600 hover:to-red-700 transition-all flex items-center justify-center gap-2 font-medium"
              >
                <RotateCcw className="w-5 h-5" />
                Reiniciar
              </button>
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <h3 className="text-lg font-semibold text-white mb-3">Estadísticas</h3>
            <div className="space-y-3">
              <div className="bg-white/10 rounded-lg p-3">
                <p className="text-blue-200 text-sm">Total Productos</p>
                <p className="text-2xl font-bold text-white">{productos.length}</p>
              </div>
              <div className="bg-white/10 rounded-lg p-3">
                <p className="text-blue-200 text-sm">Altura del Árbol</p>
                <p className="text-2xl font-bold text-white">{tree.root ? tree.root.height : 0}</p>
              </div>
              <div className="flex items-center gap-2 text-sm text-blue-200 mt-4">
                <div className="w-4 h-4 rounded-full bg-green-400"></div>
                <span>Balanceado</span>
              </div>
              <div className="flex items-center gap-2 text-sm text-blue-200">
                <div className="w-4 h-4 rounded-full bg-red-400"></div>
                <span>Desbalanceado</span>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
          <h2 className="text-xl font-semibold text-white mb-4">Visualización del Árbol AVL</h2>
          <div className="bg-slate-800/50 rounded-xl p-4 overflow-x-auto">
            {tree.root ? (
              <svg width="100%" height="500" key={refreshKey}>
                <TreeNode node={tree.root} x={400} y={50} level={0} />
              </svg>
            ) : (
              <div className="text-center py-20 text-blue-200">
                <Package className="w-16 h-16 mx-auto mb-4 opacity-50" />
                <p className="text-lg">No hay productos en el árbol</p>
                <p className="text-sm mt-2">Agrega productos para comenzar</p>
              </div>
            )}
          </div>
        </div>

        {productos.length > 0 && (
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 mt-6">
            <h3 className="text-lg font-semibold text-white mb-4">Lista de Productos (ordenados por ID)</h3>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3">
              {productos.map((prod) => (
                <div key={prod.id} className="bg-white/10 rounded-lg p-3 border border-white/20">
                  <p className="text-blue-200 text-xs">ID: {prod.id}</p>
                  <p className="text-white font-medium truncate">{prod.nombre}</p>
                  <p className="text-green-300 font-semibold">${prod.precio}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
