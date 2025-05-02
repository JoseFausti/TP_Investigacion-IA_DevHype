import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [products, setProducts] = useState([]);
  const [sortBy, setSortBy] = useState("name");
  const [ascending, setAscending] = useState(true);

  useEffect(() => {
    fetchProducts();
  }, [sortBy, ascending]);

  const fetchProducts = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/products?sort_by=${sortBy}&ascending=${ascending}`);
      setProducts(response.data);
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  return (
    <div className="container">
      <h1>Product Sorter</h1>
      <div className="controls">
        <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
          <option value="name">Sort by Name</option>
          <option value="price">Sort by Price</option>
        </select>
        <button onClick={() => setAscending(!ascending)}>
          {ascending ? "Ascending" : "Descending"}
        </button>
      </div>
      <div className="products-grid">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            <h3>{product.name}</h3>
            <p>Price: ${product.price.toFixed(2)}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
