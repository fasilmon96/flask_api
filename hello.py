from itertools import product

from flask import Flask,jsonify

#url http://127.0.0.1:5000/products
class Product:
      def __init__(self,product_id,name,price,stock):
           self.id = product_id
           self.name = name
           self.price = price
           self.stock = stock
products = [
     Product(product_id=100,name="ഇന്ത്യയില്‍ ഏറ്റവും കൂടുതല്‍ കാണപ്പെടുന്ന മണ്ണ് ?",price=500,stock=5),
     Product(product_id=101,name="Apple",price=600,stock=12),
     Product(product_id=102,name="Redmi",price=700,stock=13),
     Product(product_id=103,name="Vivo",price=300,stock=6),
     Product(product_id=100,name="Realme",price=900,stock=15),
]

def productToJson(product: Product):
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,

    }
app = Flask("APi App")

@app.route("/products",methods=["GET"])
def getAllProducts():
    print("called getAllProducts")
    productList = []
    for product in products:
        productList.append(productToJson(product))
    return jsonify({"products" : productList})
if __name__ == '__main__':
     app.run(debug=True ,host='0.0.0.0', port=5000)


