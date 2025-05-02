import React, { useEffect, useState } from 'react';

type Product = {
  id: number;
  name: string;
  price: number;
};

const ProductList = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [sortBy, setSortBy] = useState<'name' | 'price'>('name');

  useEffect(() => {
    fetch('http://localhost:5000/api/products')
      .then(res => res.json())
      .then(data => setProducts(data));
  }, []);

  const sortedProducts = [...products].sort((a, b) => {
    if (sortBy === 'price') return a.price - b.price;
    return a.name.localeCompare(b.name);
  });

  return (
    <div>
      <h2>Productos</h2>
      <label>Ordenar por: </label>
      <select onChange={(e) => setSortBy(e.target.value as 'name' | 'price')}>
        <option value="name">Nombre</option>
        <option value="price">Precio</option>
      </select>

      <ul>
        {sortedProducts.map(product => (
          <li key={product.id}>
            {product.name} - ${product.price.toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
