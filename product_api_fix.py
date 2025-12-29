from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from decimal import Decimal
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stockflow.db'
db = SQLAlchemy(app)

# Models (minimal for demonstration)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    warehouse_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()

    # Input validation
    required_fields = ['name', 'sku', 'price', 'warehouse_id']
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}, 400

    try:
        # Create product
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data['price']))
        )
        db.session.add(product)
        db.session.flush()  # fetch product.id without commit

        # Create inventory entry
        inventory = Inventory(
            product_id=product.id,
            warehouse_id=data['warehouse_id'],
            quantity=max(0, data.get('initial_quantity', 0))
        )
        db.session.add(inventory)

        # Atomic commit
        db.session.commit()

        return {
            "message": "Product created successfully",
            "product_id": product.id
        }, 201

    except IntegrityError:
        db.session.rollback()
        return {"error": "SKU must be unique"}, 409

    except Exception:
        db.session.rollback()
        return {"error": "Internal server error"}, 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
