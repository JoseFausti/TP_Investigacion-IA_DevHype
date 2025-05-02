from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api/products', methods=['GET'])
def get_products():
    with open('products.json') as f:
        products = json.load(f)
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)