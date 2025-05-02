import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
    const [products, setProducts] = useState([]);
    const [orderBy, setOrderBy] = useState("name");

    useEffect(() => {
        axios.get(`http://localhost:8000/products?order_by=${orderBy}`)
            .then(response => setProducts(response.data))
            .catch(error => console.error("Error al obtener productos", error));
    }, [orderBy]);

    return (
        <div>
            <h1>Carrito de Compras</h1>
            <select onChange={(e) => setOrderBy(e.target.value)}>
                <option value="name">Ordenar por Nombre</option>
                <option value="price">Ordenar por Precio</option>
            </select>
            <ul>
                {products.map(product => (
                    <li key={product.id}>
                        {product.name} - ${product.price}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;
